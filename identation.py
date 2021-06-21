#examples on indentation in python

# one way

function foo() {
    if ($maybe) {
        do_it_now();
        again();
    } else {
        abort_mission();
    }
    finalize();
}

# another way

function foo()
{
    if ($maybe)
    {
        do_it_now();
        again();
    }
    else
    {
        abort_mission();
    }
    finalize();
}
