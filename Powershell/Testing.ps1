$srcpath = "C:\Users\prathamsharma\Downloads\TestingPurpose\Subfolders1"
$dstpath = "C:\Users\prathamsharma\Downloads\TestingPurpose\Subfolders2"

for($i=1;$i -le 50;$i++)
{
New-Item -path $srcpath -name "TypeATest$i.txt"
}
for($i=51;$i -le 100;$i++)
{
New-Item -path $dstpath -name "TypeBTest$i.txt"
}

