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
% git clone http://localhiost:8080/git/example.git
```


## Appendix

### Docker memo

Delete all containers:

```shell-session
% docker ps -aq | xargs docker rm
```

Delete all images:

```shell-session
% docker images -aq | xargs docker rmi -f
```
