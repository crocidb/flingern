---
title: "Getting Started"
menu: "Getting Started"
---

## Installing

Through **pip**:

```
pip install flingern
```

## Creating a new site

```
flingern new helloworld
```

The structure should be:

```
helloworld:
    | site.yaml
    | content
        | index.md
```

## Building site

Once your within the site root:

```shell
flingern build .
```

## Serving for development

```shell
flingern serve . --watch
```

The `--watch` flag will watch for changes within your site's root, and will rebuild it automatically.

