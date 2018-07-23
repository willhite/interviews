<?php
    /**
     * Waits for a single character of input and returns it.
     * @return string
     */
    function get_input() {
        $term = `stty -g`;
        system('stty raw opost -echo');
        $c = fread(STDIN, 1);
        system("stty '" . $term . "'");
        return $c;
    }

    echo "Waiting for input...\n";
    $ch = get_input();
    echo "Got input $ch";
?>
