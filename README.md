# Quiet Ember Theme

A dark Visual Studio Code theme with warm accents, a charcoal background and clear distinctions between Python syntax categories. Based on the feel and core syntax colors of the JetBrains Dark editor scheme, with additional distinctions for Python attributes and parameters.

## Preview

![Quiet Ember — a fictional library example in Python with Pylance](assets/python-palette.png)

The preview uses a **fully fictional library example written for this theme**, rendered with the theme palette to show Python special methods such as `__init__` and `__str__` in bright purple. Source: [examples/palette.py](examples/palette.py).

## Install

Install **Quiet Ember Theme** from [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Toximiner.quiet-ember-theme), then open **Preferences: Color Theme** from the Command Palette and choose **Quiet Ember**.

```sh
code --install-extension Toximiner.quiet-ember-theme
```

You can also download a `.vsix` from [GitHub Releases](https://github.com/Toximiner/quiet-ember-theme/releases) and run **Extensions: Install from VSIX…**.

## Palette

| Category | Color | Example |
| --- | --- | --- |
| Classes and user-defined types | Neutral gray | `Book`, `Status` |
| Built-in Python types | Lavender | `int`, `str`, `list` |
| Built-in functions | Lavender | `len`, `print`, `next` |
| Functions and methods | Blue | `make_report`, `book.reserve` |
| Python special methods | Bright purple | `__init__`, `__str__` |
| Enum values and readonly variables | Sand | `Status.RESERVED` |
| Attributes | Slate blue | `self.copies`, `book.title` |
| `self` and `cls` | Muted purple | `self`, `cls` |
| Function parameters | Pale cyan | `reader`, `days` in a definition |
| Keyword argument names | Burnt orange | `days=14` |
| Python class keyword | Golden yellow | `class` |
| Python function keyword | Green | `def` |
| Other Python keywords | Warm orange | `return`, `if`, `raise` |
| Strings | Green | `"Ocean Stories"` |
| Numbers | Teal | `12`, `1.25` |
| Comments | Muted gray | `# explanation` |

The theme includes editor, sidebar, tabs, menus, terminal, diff and Git status colors. Brackets use a consistent neutral color rather than a rainbow.

Peek View uses a muted amber highlight for the selected reference, including locations opened from Universal Usage Lens. This keeps navigation highlights visible without the bright default accent.

Built-in functions such as `len` and `print` are predefined Python symbols, not reserved keywords. They use the same lavender color as built-in types. Python keywords follow the PyCharm reference: `class` is golden yellow, `def` is green and other keywords such as `return` are warm orange.

Palette references: JetBrains' [Dark scheme](https://github.com/JetBrains/intellij-community/blob/master/platform/platform-resources/src/themes/expUI/expUI_darkScheme.xml) and [Python highlighter](https://github.com/JetBrains/intellij-community/blob/master/python/python-syntax-core/src/com/jetbrains/python/highlighting/PyHighlighter.java). This is an adaptation for VS Code and Pylance, with deliberate differences such as sand enum values and distinct attribute colors.

## Python highlighting

For the full result shown above, install Microsoft's **Python** and **Pylance** extensions. Semantic highlighting is enabled by the theme. If you explicitly disabled it, set:

```json
"editor.semanticHighlighting.enabled": "configuredByTheme"
```

TextMate grammar colors remain available without Pylance, but the distinction between types, attributes and ordinary variables may be less precise. Other languages use the theme's general syntax rules; their semantic colors depend on the installed language extension. User color customizations can override the palette.

## Development and releases

```sh
npm ci
npm run package
```

The theme contains no executable extension code. GitHub Actions builds the VSIX and attaches it, with a SHA256 checksum, to version-tag releases. Marketplace publishing uses GitHub OIDC Trusted Publishing.

## License

[MIT](LICENSE). This is an independent theme, not affiliated with JetBrains or Microsoft.
