const Koa = require('koa');
const logger = require('koa-logger');
const fs = require('fs');
const app = new Koa();

app.use(logger());
app.use(async ctx => {
  let filepath = ctx.query.filepath || 'index.html';
  if (filepath.startsWith('/')) {
    ctx.body = 'You cant trick me this time!';
    return;
  }

  // This uses a regular expression.  Read more about them here:
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
  filepath = filepath.replace(/..\//g, '');
  // Now there is no way you can traverse!

  ctx.body = fs.readFileSync(filepath, {encoding: 'utf8'});
});

console.log('http://0.0.0.0:5000/')
app.listen(5000);
