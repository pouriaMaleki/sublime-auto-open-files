Personalized Sublime Text 3 Plugin To Open .styl (Stylus) With .ls (Livescript)

Is it usefull?

If you using Webpack, Livescript and Stylus and importing your styles to your code this might be usefull for you.


Here is my Webpack config for loading styl files:

    loader: "css?module"

And here is my way to store my components:

    namespaces
      pageStuff
        Footer.ls
        Footer.styl
        Header.ls
        Header.styl

So this plugin will help with automatically open styl file if I open ls and also open ls if I open styl file.

Keyboard shortuct to open Styl (or ls) of this component is `Alt + Shift + S` and the command is `Open Styl With Ls`

Setting in Settings - User (Preferences.sublime-settings):

Activate auto open: `"open_styl_with_ls": true`

It also can be forced to open styl (or ls) just when you are in side by side mode (Alt + Shift + 2)

`"open_styl_with_ls_only_if_2_groups": true`

