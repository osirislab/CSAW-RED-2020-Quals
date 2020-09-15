const Koa = require('koa');
const logger = require('koa-logger');
const fs = require('fs');
const app = new Koa();

app.use(logger());
app.use(async ctx => {
  const filepath = ctx.query.filepath || 'index.html';
  ctx.body = fs.readFileSync(filepath, {encoding: 'utf8'});
});

console.log('http://0.0.0.0:5000/')
app.listen(5000);
