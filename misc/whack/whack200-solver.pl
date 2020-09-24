#!/usr/bin/perl
use strict;
use warnings;
use IO::Socket::INET;

# flush after every write
$| = 1;

my $socket = new IO::Socket::INET (
	PeerHost => '127.0.0.1',
	PeerPort => '9933',
	Proto => 'tcp',
) or die "Cannot create socket: $!\n";

my $logfile = '/tmp/solve.log';
open LOG, ">$logfile" or die "Cannot open $logfile for writing: $!\n";

my $data = '';
my $found = 0;
while ($found < 2) {
	my $buf;
	$socket->recv($buf, 1024);
	$data .= $buf;
	if (length($buf) < 1024) {
		$found = process($data);
		$data = '';
	}
}

close LOG;
$socket->close();

#-----------------------------------------------------------------------------------------------------------------------------------
sub process
{
	my $data = shift;
	my @lines = split "\n", $data;

	my $found     =  0;  # 0 if not found, 1 if found, 2 if winner
	my $row       = -1;  # Row where mole was found
	my $col       =  0;  # Column where mole was found
	my $blank     =  0;  # Non-zero if preceding line was blank
	my $space     = '';  # String that holds space
	my $non_space = '';  # String that holds non-space
	foreach my $line (@lines) {
		print LOG "-->$line<--\n";
		if ($line =~ m/WINNER|Ouch/) {                  # Check for winner or ouch message
			$found  = 2;
		} elsif ($line =~ m/^Whack \(row col\)/) {      # Check for end of board
			last;
		} elsif ($line =~ m/^ *$/) {                    # Check for blank lines
			$blank = 1;
		} elsif (($line !~ m/^Level/) and not $found) { # Process remaining lines if mole hasn't been found

			# Parse start of each row of the board
			if ($blank) {
				$blank = 0;
				$row++;

				if ($row == 0) {
					# Get spaces
					my $tmp = $line;
					$tmp =~ s/[^ ]+/:/g;
					my @spaces = split ':', $tmp;
					$space = $spaces[1]; # Skip leading space, since it is too small

					# Get non-spaces
					$tmp = $line;
					$tmp =~ s/ +/ /g;
					my @non_spaces = split ' ', $tmp;
					$non_space = $non_spaces[0];
				}
			}

			# Check for the mole's nose
			my $index = index $line, '" O "';
			if ($index != -1) {
				# Find the column that the mole is in
				my $str = $non_space;
				while (length($str) < $index) {
					$str .= $space . $non_space;
					$col++;
				}
				$found = 1;
			}
		}
	}

	if ($found > 1) {
		print $data; # Print winner or ouch message
	} else {
		$data = "$row $col\n";
		print LOG "\nMole is on $data";
		$socket->send($data);
	}
	return $found;
}
