---
title: "Galleries"
galleries:
    - name: gallery1
      images:
        - images/another-test.jpg
        - images/image-test.jpg
    - name: gallery2
      images:
        - images/image-test-*.jpg
---

Pages can contain several galleries. You have to define them on the page metadata:

```yaml
galleries:
    - name: gallery1
      images:
        - docs/images/*.jpg
```

Then add to the page like this:

```markdown
!![gallery1]
```

And that's how it will look like:

!![gallery1]

Great, right?

!![gallery2]

Another gallery!
