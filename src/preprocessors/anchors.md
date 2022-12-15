# Anchors

Preprocessor which allows to use arbitrary anchors in Foliant documents.

## Installation

```bash
$ pip install foliantcontrib.anchors
```

## Config

To enable the preprocessor, add anchors to preprocessors section in the project config:

```yaml
preprocessors:
    - anchors
```

The preprocessor has some options, but most probably you won't need any of them:

```yaml
preprocessors:
    - anchors:
        element: '<span id="{anchor}"></span>'
        tex: False
        anchors: True
        custom_ids: False
```

`element`
:   Template of an HTML-element which will be placed instead of the `<anchor>` tag. In this template `{anchor}` will be replaced with the tag contents. Ignored when tex is `True`. Default: `'<span id="{anchor}"></span>'`

`tex`
:   If this option is `True`, preprocessor will try to use TeX-language anchors: `\hypertarget{anchor}{}`. Default: `False`

> Notice, this option will work only with `pdf` target. For all other targets it is set to `False`.
`anchors`
:   If this options is `True`, anchors tag will be processed. Turn off if you only want to process custom IDs. Default: `True`

`custom_ids`
:   Since version 1.0.5 preprocessor Anchors can also process Pandoc-style custom IDs. Set this option to `True` to do that. Default: `False`.

## Usage

**anchors**

Just add an `anchor` tag to some place and then use an ordinary Markdown-link to this anchor:

```html
...

<anchor>limitation</anchor>
Some important notice about system limitation.

...

Don't forget about [limitation](#limitation)!
