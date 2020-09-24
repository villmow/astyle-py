
options = {
    # brace
    # http://astyle.sourceforge.net/astyle.html#_Brace_Style_Options
    "style": [
        "allmann",
        "kr",
        "stroustrup",
        "whitesmith",
        "vtk",
        "ratliff",
        "gnu",
        "linux",
        "horstmann",
        "1tbs",
        "google",
        "mozilla",
        "pico",
        "lisp",
        "python",
    ],
    # tab
    # http://astyle.sourceforge.net/astyle.html#_Tab_Options
    # default indent    indent=spaces    indent=tab    indent=force‑tab    --indent=force‑tab‑x
    "indent": {
        "spaces": list(range(2,21)),
        "tab": list(range(2,21)),
        "force-tab": list(range(2,21)),
        "force-tab-x": list(range(2,21)),
    },
    # Brace Modify Options
    "attach-namespaces": [],
    "attach-classes": [],
    "attach-inlines": [],
    "attach-extern-c": [],
    "attach-closing-while": [],

    # Indentation Options
    "indent‑classes": [],
    "indent‑modifiers": [],
    "indent‑switches": [],
    "indent‑cases": [],
    "indent‑namespaces": [],
    "indent‑after‑parens": [],
    "indent‑continuation": [],
    "indent‑labels": [],
    "indent‑preproc‑block": [],
    "indent‑preproc‑define": [],
    "indent‑preproc‑cond": [],
    "indent‑col1‑comments": [],
    "min‑conditional‑indent": list(range(4)),
    "max‑continuation‑indent": list(range(40,121)),

    # padding options
    "break-blocks": [],
    "break-blocks=all": [],
    "pad-comma": [],
    "pad-paren": [],
    "pad-paren-out": [],
    "pad-first-paren-out ": [],
    "pad-paren-in": [],
    "pad-header": [],
    "unpad-paren": [],
    "delete-empty-lines": [],
    "fill-empty-lines": [],
    "align-pointer": [
        "type",
        "middle",
        "name",
    ],
    "align-reference": [
        "none",
        "type",
        "middle",
        "name",
    ],
    "break‑closing‑braces": [],
    "break‑elseifs": [],
    "break‑one‑line‑headers": [],
    "add‑braces": [],
    "add‑one‑line‑braces": [],
    "remove‑braces": [],
    "break‑return‑type": [],
    "attach‑return‑type": [],
    "keep‑one‑line‑blocks": [],
    "keep‑one‑line‑statements": [],
    "convert‑tabs": [],
    "close‑templates": [],
    "remove‑comment‑prefix": [],
    "max‑code‑length": list(range(50,201)),
    "break‑after‑logical": [],
    "mode": ["c", "cs", "java"],

}
