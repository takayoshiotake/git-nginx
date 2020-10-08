# git-nginx

This is an example of Git Smart HTTP server with Nginx, on Docker.


## Get started

```shell-session
% docker-compose up --build
```

### Make a new bare repository

You can make a new bare repository on `git` directory.

```shell-session
% mkdir example.git && cd "$_"
% git init --bare --shared && git config http.receivepack true
```

### Clone repository

e.g.

```shell-session
% git clone http://localhost:8080/git/example.git
```

### Add authentication to repository

Basic authentication is enabled when repository has `.git-nginx/passwd` file.

e.g. username is `user` and password is `pass`

```shell-session
% cd example.git
% mkdir -p .git-nginx && cd "$_"
% echo user:$(openssl passwd -6 pass) >> passwd
% cat passwd
user:$6$zpn/Nlf1zpa.RzsB$VtNvmT6BdIoyXAGwV8Ix7AeCwgDV7l477lOmiWv6k0rx1t5OybEPQ9Ty4k5rnLOhnDBdu5rN90XNyv6pprJDP1
```

## Appendix

### Docker memo

Run bash on conatiner:

```shell-session
% docker-compose run --service-ports git-nginx bash
```

Delete all containers:

```shell-session
% docker ps -aq | xargs docker rm
```

Delete all images:

```shell-session
% docker images -aq | xargs docker rmi -f
```
