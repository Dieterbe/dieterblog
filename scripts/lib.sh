# exclude harmless/expected content and diff markers
function compare() {
  diff -r $1 $2 |
    grep -v 'light dark' |                                           # https://github.com/Dieterbe/hugo-blog-awesome/commit/f5c6e01b7ccbef68f1410d6dac8412116427d0ad
    grep -vE '^---$|^[a-z]$|^[0-9]+(,[0-9]+)?[acd][0-9]+(,[0-9]+)?$' # diff markers
}
