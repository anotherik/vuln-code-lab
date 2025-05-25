<?php
if (isset($_GET['filename'])) {
    $file = $_GET['filename'];

    $safe_file = escapeshellarg($file);
    $cmd = "convert uploads/$safe_file -resize 200x200 uploads/resized_$safe_file";
    $output = shell_exec($cmd);

    echo "<pre>$output</pre>";
} else {
    echo "Missing filename.";
}
?>
