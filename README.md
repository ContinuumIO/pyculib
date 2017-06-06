# Pycudalib

Description...

Building Documentation
----------------------

Documentation is stored in the `doc` folder, and should be built with:

```
$ make SPHINXOPTS=-Wn clean html
```

This ensures that the documentation renders without errors. If errors occur,
they can all be seen at once by building with:

```
$ make SPHINXOPTS=-n clean html
```

However, these errors should all be fixed so that building with `-Wn` is
possible prior to merging any documentation changes or updates.
