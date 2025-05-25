<?php
if (isset($_GET['filename'])) {
    $file = $_GET['filename'];

    $cmd = "convert uploads/$file -resize 200x200 uploads/resized_$file";
    $output = shell_exec($cmd);

    echo "<pre>$output</pre>";
} else {
    echo "Missing filename.";
}
?>
