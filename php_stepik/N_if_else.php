// Дано число N. Если число больше 10, то увеличьте на 100, иначе уменьшите на 30.

<?php
fscanf(STDIN,"%d",$N); 

if ($N > 10)
{
   echo $N+100;
}

if ($N < 10)
{
   echo $N-30;
}
?>
