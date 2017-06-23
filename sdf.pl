use strict;
use warnings;
# use File::Slurp;
my %hash;
$/=undef;
my $i=0;
open(IN, '<ligands.sdf');
open(OUT, '>ligandsn.sdf');
my @mol = split('\$\$\$\$\n',<IN>);
# print $mol[100];
foreach (@mol) {
    unless (/IC50 \(nM\)>\n>/ | /Kd \(nM\)>\n>/) {
        /BindingDB Ligand Name>\n(.*)/;
        # print $1;
        my $bdid = $1;
        $_ =~s/^.*/$bdid/;
        # $_ = $bdid.$_;
        $hash{$bdid}= $_."\$\$\$\$"."\n";
        # $i++;

    }

} 

foreach (sort keys %hash) {
    print OUT "$hash{$_}";
  }

close IN;
close OUT;