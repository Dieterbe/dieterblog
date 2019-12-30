## Dieterblog

public-real contains the website that is live right now, generated using hugo 0.16
Trying to update to a newer hugo but running into a bunch of problems. For that work, see upgrade-hugo-current branch

```
mkdir hugo-0.16 && cd hugo-0.16
wget https://github.com/gohugoio/hugo/releases/download/v0.16/hugo_0.16_linux-64bit.tgz
tar xzf hugo_0.16_linux-64bit.tgz
cd ..
./hugo-0.16/hugo --config config-prod.toml -d public-real
```
