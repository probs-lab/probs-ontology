# PRObs Ontology Specification

This documentation has been generated using the [Widoco](https://github.com/dgarijo/Widoco).

<details>
  <summary>Options used</summary>

```sh
-ontFile ontology/probs.ttl
    'Load a local ontology file to document.'
-outFolder release/MAJOR.MINOR.PATCH/
    'Specifies the name of the folder where to save the documentation.'
-getOntologyMetadata
    'Extract ontology metadata from the given ontology.'
-oops
    'Create an html page with the evaluation from the OOPS service (http://oops.linkeddata.es/).'
-rewriteAll
    'Replace any existing files when documenting an ontology (e.g., from a previous execution)'
-crossRef:
    'ONLY generate the overview and cross reference sections. The index document will NOT be generated. The htaccess, provenance page, etc., will not be generated unless requested by other flags. This flag is intended to be used only after a first version of the documentation exists.'
-htaccess
    'Create a bundle for publication ready to be deployed on your Apache server.'
-webVowl
    'Create a visualization based on WebVowl in the documentation.'
```

</details>

Different modes are suggested depending on the specific case:

- [Generate from scratch](#generate-from-scratch)
  - useful as a development version
- [Generate only overview and cross-reference sections](#generate-only-overview-and-cross-reference-sections)
  - useful in case of minor changes
- [Re-generate all](#re-generate-all)
  - useful in case of major changes

## Generate from scratch

The command used to generate the development version is:

```sh
java -jar '[...]widoco[...].jar' -ontFile 'ontology/probs.ttl' -outFolder 'release/' -getOntologyMetadata -oops -htaccess -webVowl
```

This version can be used to visualise it locally (using a local server) and to evaluate the ontology (using the OOPS! service).

## Generate only overview and cross-reference sections

To generate the public documentation to deploy using GitHub Pages, a copy of an existing deployed version needs to be created (using the current version number) and the following command should be used:

```sh
java -jar '[...]widoco[...].jar' -ontFile 'ontology/probs.ttl' -outFolder 'release/MAJOR.MINOR.PATCH/' -getOntologyMetadata -webVowl -crossRef -rewriteAll
```

Then, if necessary, `introduction-en.html`, `description-en.html`, and `references-en.html` need to be updated.

This is useful when there are minor changes in the ontology since it does not update most of the documentation (for instance, it does not update the "Namespace declarations" table).

## Re-generate all

To generate the public documentation to deploy using GitHub Pages, the following command should be used:

```sh
java -jar '[...]widoco[...].jar' -ontFile 'ontology/probs.ttl' -outFolder 'release/MAJOR.MINOR.PATCH/' -getOntologyMetadata -webVowl -rewriteAll
```

Then, some changes need to be applied to the HTML files in the `sections` folder.

> It is worth noting that [there is an issue opened about this](https://github.com/dgarijo/Widoco/issues/604). Hopefully we will not have to change them any more in the future.

The following should be added in the `introduction-en` file:

<details>
  <summary>Custom content</summary>

```html
<p>
    This is the documentation of the "Physical Resources Observatory" (PRObs) ontology.
</p>

<div id="material-flow-systems">
    <h3 class="list">Material flow systems</h3>
    <p>
        The core conceptual model is consistent with the <em>bipartite directed graphs</em> described by [<a href="#ref-1">1</a>]:
    </p>
    <ul>
        <li>
            <p>
                A <em>Process</em> is where events/transformations happen.
            </p>
        </li>
        <li>
            <p>
                The things going in and out are <em>Objects</em> (taken broadly, to include goods, materials, energy, and services).
            </p>
        </li>
        <li>
            <p>
                A <em>flow</em> is the movement of an object in or out of a process.
            </p>
        </li>
    </ul>
    <p>
        A material flow system consists of a set of processes within a boundary, defined in both space and time.
    </p>
</div>
```

</details>

replacing the placeholder text.

The following should replace the content in the `description-en` file:


<details>
  <summary>Custom content</summary>

```html
<h2 id="desc" class="list">
    Physical Resources Observatory (PRObs) Ontology: Description
    <span class="backlink">
        back to <a href="#toc">ToC</a>
    </span>
</h2>

<p>
    The data model proposed [<a href="#ref-1">1</a>] describes three components of a data point: value, metadata, and "system location".
    The value can be a simple numerical value with associated physical units, or could account for uncertain values by defining probability distributions or bounds.
    The metadata includes provenance information.
    The system location is the component specific to MEFA: it associates the data point with its context.
</p>

<p>
    To represent this, we introduce the concept of an <em>Observation</em> to represent an individual data point and its value, linked to its system location.
    We then introduce concepts describing types of materials/goods, and how they are related.
    Full details are available below and in [<a href="#ref-2">2</a>].
</p>

<p>
    It is worth noting that the ontology links to several external vocabularies:
    <a href="http://www.w3.org/TR/prov-o">PROV</a> for data provenance,
    <a href="http://qudt.org">QUDT</a> for physical units,
    <a href="https://www.geonames.org/ontology">Geonames</a> for spatial regions,
    and <a href="https://www.w3.org/TR/owl-time">OWL-Time</a> for time.
</p>
```

</details>

The following should replace the content in the `references-en` file:


<details>
  <summary>Custom content</summary>

```html
<h2 id="ref" class="list">
    References
    <span class="backlink">
        back to <a href="#toc">ToC</a>
    </span>
</h2>

<dl>
    <dt id="ref-1">
        [1]
    </dt>
    <dl>
        Stefan Pauliuk, Guillaume Majeau-Bettez, Daniel B. Müller, Edgar G. Hertwich.
        <br/>
        Toward a Practical Ontology for Socioeconomic Metabolism.
        <br/>
        <em>Journal of Industrial Ecology</em>
        <a href="https://doi.org/10.1111/jiec.12386">doi:10.1111/jiec.12386</a>.
    </dl>
    <dt id="ref-2">
        [2]
    </dt>
    <dl>
        Stefano Germano, Carla Saunders, Ian Horrocks, Rick Lupton.
        <br/>
        Use of Semantic Technologies to Inform Progress Toward Zero-Carbon Economy.
        <br/>
        <em>Proceedings of ISWC 2021</em>
        <a href="https://doi.org/10.1007/978-3-030-88361-4_39">doi:10.1007/978-3-030-88361-4_39</a>.
    </dl>
</dl>
```

</details>

## Cleaning documentation

The tools included in the documentation contain resources hosted by other entities.
We want to remove them to avoid privacy issues and be more future-proof.

Moreover, we might want to improve the documentation by tweaking some parts of it.

Note that these _tweaks_ are only needed when we re-generate those files.

### Remove Google Fonts

A _Google Fonts_ `import` is included in the file `webvowl/css/webvowl.app.css`.
We can simply remove it.

### Shields.io badges

Several badges are included from _Shields.io_.
These are more "difficult" to remove since they are automatically generated in the `index-en.html` file.

The badges currently used have been downloaded in the folder `images` (if other badges are required, they should be uploaded here as well).
Therefore, we simply need to replace `https://img.shields.io/badge` with `images` and remove `License-https://creativecommons.org/licenses/by/` and `Format-RDF/`.

### Namespace declarations

And, the "Namespace declarations" table could be ordered lexicographically.

> It is worth noting that [there is an issue opened about this](https://github.com/dgarijo/Widoco/issues/610). Hopefully we will not have to change it any more in the future.

<details>
  <summary>Example</summary>

```html
<div id="namespacedeclarations">
    <h3 id="ns" class="list">
        Namespace declarations
    </h3>
    <div id="ns" style="margin: auto; width:fit-content">
        <table>
            <caption>
                <a href="#ns">Table 1</a>: Namespaces used in the document
            </caption>
            <tbody>
                <tr>
                    <td><b>probs</b></td>
                    <td>&lt;http://w3id.org/probs-lab/ontology#&gt;</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td><b>cc</b></td>
                    <td>&lt;http://creativecommons.org/ns&gt;</td>
                </tr>
                <tr>
                    <td><b>dc</b></td>
                    <td>&lt;http://purl.org/dc/elements/1.1&gt;</td>
                </tr>
                <tr>
                    <td><b>dcterms</b></td>
                    <td>&lt;http://purl.org/dc/terms&gt;</td>
                </tr>
                <tr>
                    <td><b>foaf</b></td>
                    <td>&lt;http://xmlns.com/foaf/0.1&gt;</td>
                </tr>
                <tr>
                    <td><b>gn</b></td>
                    <td>&lt;http://www.geonames.org/ontology&gt;</td>
                </tr>
                <tr>
                    <td><b>org</b></td>
                    <td>&lt;http://www.w3.org/ns/org&gt;</td>
                </tr>
                <tr>
                    <td><b>owl</b></td>
                    <td>&lt;http://www.w3.org/2002/07/owl&gt;</td>
                </tr>
                <tr>
                    <td><b>prov</b></td>
                    <td>&lt;http://www.w3.org/ns/prov&gt;</td>
                </tr>
                <tr>
                    <td><b>qudt</b></td>
                    <td>&lt;http://qudt.org/schema/qudt&gt;</td>
                </tr>
                <tr>
                    <td><b>rdf</b></td>
                    <td>&lt;http://www.w3.org/1999/02/22-rdf-syntax-ns&gt;</td>
                </tr>
                <tr>
                    <td><b>rdfs</b></td>
                    <td>&lt;http://www.w3.org/2000/01/rdf-schema&gt;</td>
                </tr>
                <tr>
                    <td><b>time</b></td>
                    <td>&lt;http://www.w3.org/2006/time&gt;</td>
                </tr>
                <tr>
                    <td><b>vann</b></td>
                    <td>&lt;http://purl.org/vocab/vann&gt;</td>
                </tr>
                <tr>
                    <td><b>xsd</b></td>
                    <td>&lt;http://www.w3.org/2001/XMLSchema&gt;</td>
                </tr>
                <tr>
                    <td><b>xml</b></td>
                    <td>&lt;http://www.w3.org/XML/1998/namespace&gt;</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>
```

</details>

### Authors order

The system automatically sorts the authors lexicographically.
We need to manually re-order them in the `index-en.html` file.

> It is worth noting that [there is an issue opened about this](https://github.com/dgarijo/Widoco/issues/608). Hopefully we will not have to change it any more in the future.
