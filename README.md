# readee

Library for export webpage to reader mode html.

## usage

```
import readee
beautiful_soup_html = readee.export(url = webpage_url)
```

optional args:
- content: raw webpage, will skip url fetching
- list_replace: will replace list, usually for telegraph export
- preserve_link: keep links
- include_title: keep title
- move_head_photo: try move head photo to top


## how to install

`pip3 install readee`