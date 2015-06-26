#! /bin/bash

_cryptotools_opts () {
    local cur prev opts
    COMPREPLY=()

    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD - 1]}

    CIPHERS="caesar-shift affine-shift vigenere"

    case "$prev" in
        "ciphers")
            COMPREPLY=($(compgen -W "-d $CIPHERS" -- $cur)) ;;
        "-d")
            COMPREPLY=($(compgen -W "$CIPHERS" -- $cur)) ;;
        "analysis")
            COMPREPLY=($(compgen -W "caesar-shift-cracker affine-shift-cracker column-analysis" -- $cur)) ;;
        *)
            COMPREPLY=($(compgen -W "ciphers analysis -i -f -h --help" -- $cur)) ;;
    esac;

    return 0;
}

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
alias ct="python $DIR/ct.py"

complete -F _cryptotools_opts ct
