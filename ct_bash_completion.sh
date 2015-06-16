#! /bin/bash

_cryptotools_opts () {
    local cur prev opts
    COMPREPLY=()

    cur=${COMP_WORDS[COMP_CWORD]}

    if (( $COMP_CWORD == 1 )) ; then
        COMPREPLY=( $(compgen -W 'ciphers analysis' -- $cur))
    fi;

    if (( $COMP_CWORD >= 2)) ; then
        action=${COMP_WORDS[1]}
        case "$action" in
            'ciphers')
                COMPREPLY=($(compgen -W 'caesar-shift affine-shift vigenere' -- $cur)) ;;
            'analysis')
                COMPREPLY=($(compgen -W 'caesar-shift-cracker affine-shift-cracker' -- $cur)) ;;
        esac;
    fi;

    return 0;
}

# Need a better method than this
alias ct='python ct'

complete -F _cryptotools_opts ct
