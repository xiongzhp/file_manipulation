use Chemistry::File::SDF;

my @mols = Chemistry::Mol->read('/Volumes/WIN/Specs_SC_10mg_Aug2016.sdf');
my @items;
for ( 1 .. 3113 )
{
push @items, $mols[ rand @mols];
}

Chemistry::Mol->write('/Volumes/WIN/ramdom_specs_3k.sdf', mols => \@items);
