use strict;
use warnings;
# use File::Slurp;
my %hash;
my %hash1;
$/=undef;
my $i=0;
open(IN, '<4bkj_ranked2.sdf');
open(IN1, '<rank.txt');
open(OUT, '>4bkj_selected.sdf');
my @mol = split('\$\$\$\$\n',<IN>);
my @rank = split('\n',<IN1>);
foreach (@rank) {
    my $entry = "4bkj_ranked.".$_;
    # print $entry;
    $hash1{$entry}=1;
}    

# print $hash1{$entry};

# print $mol[100];
foreach (@mol) {   
    /s_m_entry_name>\n(.*)/;
    # print $1;
    my $eid = $1;
    print OUT $_."\$\$\$\$"."\n" if exists $hash1{$eid};
} 


close IN1;
close IN;
close OUT;