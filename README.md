# Quarto Report

This is a report written using a [Quarto book](https://quarto.org/docs/books/). Quarto Books are combinations of multiple documents (chapters) into a single manuscript. 

## Structure of this book

### YAML files

 - [`_quarto.yml`](_quarto.yml) : a Quarto project file which contains the initial configuration of the book.

 - [`_publish.yml`](_publish.yml) : this file is used to specify the publishing destination of the project. This file is automatically created (or updated) whenever you execute the quarto `publish command`, and is located within the project or document directory.

### Output directory:

- [`/_book`](/_book/): By default, [quarto book output](https://quarto.org/docs/books/book-output.html) is written to the _book directory of your project, this is where the final rendered [`.pdf`](/_book/3rd-Year-Report.pdf) lives.

### Markdown files

- `.qmd` and `.md` files: are markdown documents. Quarto `.qmd` files can contain a combination of markdown and executable code cells. I have some files in .qmd and others with simple .md format depending on whether I need the quarto functionality to run them or not.

### Images
- I have left the `.PNG` and `.JPG` files in the main directory instead of a subfolder because this is a small project, but if I had bigger, multiple chapters, figures could be divided into subfolders for smoother organisation. 

### BibTeX file
- [`references.bib`](references.bib) : This is where the references used in this report live. By default, Pandoc will automatically generate a list of works cited and place it in the document if the style calls for it. It will be placed in a div with the id refs if one exists, defined in the file:
- [`references.qmd`](references.qmd)
```
### References

::: {#refs}
:::
```

***Citation Style***

Quarto uses Pandoc to format citations and bibliographies. By default, Pandoc will use the [Chicago Manual of Style](https://www.chicagomanualofstyle.org/home.html) author-date format. So that is the one being used here.

If you wanted to specify a custom format of referencing, you can use CSL [(Citation Style Language)](https://citationstyles.org/). To learn how to do this, Quarto has documentation on this [here](https://quarto.org/docs/authoring/footnotes-and-citations.html).


## Requirements
- [Quarto](https://quarto.org/docs/get-started/).
- A tool to run Quarto with. I use VS Code, but you could use others like RStudio, Jupyter, Neovim, or your preferred text editor.
- If you don't have a TeX installation present on your system, the following needs to be executed once after the installation of Quarto: `quarto install tinytex`.

## If you want to run and use this report as a template

- [Fork it](https://docs.github.com/en/get-started/quickstart/fork-a-repo#use-someone-elses-project-as-a-starting-point-for-your-own-idea), then use it as a template for your own work. This way you can give credit to where your own repo came from.

## License:

'License to be confirmed'