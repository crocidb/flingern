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

```markdown
galleries:
    - name: gallery-one
      images:
        - docs/images/*.jpg
```

Then add to the page like this:

<!-- ```markdown -->
<!-- !![gallery-one] -->
<!-- ``` -->
And that's how it will look like:

!![gallery1]

Great, right?

!![gallery2]

Another gallery!
