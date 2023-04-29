
.. term-vocab:

Words and Formats used in Project
=================================

.. _terms-data:

   Data
      An item of factual information derived from measurement or research.

      Literals (numbers and letters).

.. _terms-data-element:

   Data Element
      Field or column in a data-set or data-base that stores Data.

.. _terms-data-dictionary:

   Data Dictionary
      Specifies information about a Data Element. Information includes field name, field description, data type and constraint for Data Element.

.. _terms-data-model:

   Data Model
      Representation of how to aggregate and interrelate Data defined by a Data Dictionary.

.. _terms-entity-relationship-model:

   Entity-Relationship Model
      Representation of how to aggregate and inter-relate information. An entity is a Thing capable of an independent existence and is uniquely identified. Entities are nouns. Examples: a food commodity, a food consumer, a recipe, or a food label calculation. A relationship specifies how entities are related to one another. Relationships are verbs, linking two or more nouns. Examples are: beneficial for, caused by, composed of, made from, produced by, used in. Entities and relationships have Properties, such as a distinguishing quality, a physical state, or a characteristic that is determined by a gene or group of genes.

.. _terms-context

   Context
      Discourse that surrounds a language unit and helps to determine its interpretation. For the project, the Context of the language unit is Food. In other words, the Domain-of-Context is Food.

.. _terms-vocabulary

   Vocabulary
      A listing or grouping of words that are common to a Domain-of-Context.

.. _terms-controlled-vocabulary

   Controlled Vocabulary
      Authorized words that have been preselected for a Domain-of-Context. Contrasts with natural language vocabularies, where there is no restriction on the vocabulary.

.. _terms-term

   Term
      Word in a Controlled Vocabulary that references a Description. Term is described in a Thesaurus.

.. _terms-taxonomy

   Taxonomy
      Categorization of Things (entities). Categorization is based on discrete sets. Taxonomy may have multiple forms, such as lists and hierarchies.

      Hierarchy of facets in a specific knowledge domain. Base of taxonomy is called a facet. Term in hierarchy is called facet term (FT). Code assigned to facet term is called facet term code (FTC). Taxonomy does not include predicates, formal classes, expressions or axioms.

.. _terms-metadata

   Metadata
      Same as a word in a Taxonomy.

.. _terms-thesaurus

   Thesaurus
      Provides information about a Term in a Controlled Vocabulary. Includes long name, short name or acronym, and description in form of Scope Notes and Additional Information.

.. _terms-glossary

   Glossary
      Defines words associated with a project. A word in a glossary is not necessarily a Term in a Controlled Vocabulary.

.. _terms-encyclopedia

   Encyclopedia
      The services known as Wikipedia and DBpedia. Wikipedia disambiguation associates a word with a Domain-of-Context.

.. _terms-syntax

   Syntax
      Rules for specifying Terms to create structures like phrases, sentences, and paragraphs.

.. _terms-grammar

   Grammar
      Rules for specifying a set of well-formed structures using Terms of a given Language.

.. _terms-language

   Language
      Set of Terms specified by a Syntax and sequenced according to a Grammar. Language is used to systematically define and aggregate knowledge.

.. _terms-ontology

   Ontology
      Combination of the above to express higher order activities, such as communications, translation, learning, understanding, teaching, and making decisions. More specifically, a formal way to represent entities, ideas, and events (Things). Things have Properties such as names and values. Things have Relations such as kinship and sequence of steps (ordinality) to perform a task. Things, Properties and Relations are organized by categories (Taxonomy). Knowledge - in a form that can be processed by a computer - is the categorical ordering of Things, Properties and Relations from Domain-of-Context into a Domain-of-Knowledge.

.. _terms-is-a-relationship

   IS-A relationship
      Specifies relations between abstractions (e.g. types, classes), where one class A is a subclass of another class B (and so B is a superclass of A). In other words, type A is a subtype of type B when A's specification implies B's specification. More specifically, the IS-A relationship is defined by:
   
         1) Hypernymy-Hyponymy (supertype-subtype) relations between types (classes) defining a taxonomic hierarchy, where a hyponym (subtype, subclass) has a type-of (IS-A) relationship with its hypernym (supertype, superclass)
   
         2) Holonymy-Meronymy (container-part or member) relations between types (classes) defining a possessive hierarchy.
   
.. _terms-has-a-relationship

   HAS-A relationship
      Specifies part-whole relations. Meronym is the name given to a constituent part of, the substance of, or a member of something. 'X' is a meronym of 'Y' if an X is a part of a Y. A meronym may be:
   
         1) Transitive - "Parts of parts are parts of the whole" - if A is part of B and B is part of C, then A is part of C.
   
         2) Reflexive - "Everything is part of itself" - A is part of A.
   
         3) Antisymmetric - "Nothing is a part of its parts" - if A is part of B and A !- B then B is not part of A.

.. _terms-domain

   Domain
      Set of values for a Term declared in a Relation.

.. _terms-range

   Range
      Limits for the values of a Term declared in a Relation.

.. _terms-symmetric-relationship

   Symmetric relationship
      Declaration that Terms are essentially the same and are interchangeable.

.. _terms-ontology-2

   Ontology (continuing to add precision to the word "Ontology" previously used above)
      Uses a Controlled Vocabulary to specify Things, Properties and Relations for a Domain-of-Knowledge. Defines a set of statements about a Domain-of-Knowledge. Statements in Ontomatica ontologies are implemented as Graphs.

      An ontology is a set of statements in the logical form: :class:`subject` :class:`predicate` :class:`object` where :class:`subject` and :class:`object` are facet terms.

.. _terms-faceted-classification

   Faceted Classification
      Enables assignment of a Term to multiple categories in a Taxonomy. Faceted search (a.k.a. faceted navigation or faceted browsing) is the user-interface of a faceted classification system. Users explore a collection of information by applying multiple filters (a.k.a. facet terms).

.. _terms-facet-tree

   Facet Tree
      Hierarchy of Facets in a specific Domain-of-Knowledge.

.. _terms-thing

   Thing (continuing to add precision to the word "Thing" previously used above)
      An entity capable of an independent existence that can be uniquely identified.

.. _terms-subject

   Subject
      An observer; an entity that has a relationship with another entity that exists outside of itself (an "object"). A Subject is an observer and an Object is an entity observed.

.. _terms-object

   Object
      An entity observed by a Subject.

.. _terms-item

   Item
      A Thing - associated with a Domain-of-Knowledge - that is described by one or more Terms in one or more Facet Trees. Item is comparable to Data in a Data Model and to an instance of an Entity-type in an Entity-Relationship model.

      Food record in electronic format.

.. _terms-graph

   Graph
      Composed of vertices {nodes} and lines {edges} that connect vertices. Ontomatica graphs are Directed Acyclic Graphs (DAG) that represent Things and causal Relations between them.

.. _terms-facet

   Facet and Facet Term (as defined during Facet Classification and revealed in a Facet Tree)
      Vertex {node} in a Graph. Logically, a facet is a noun. A class term (word identifying a collection of Facet Terms) is called a Facet. A type term (instances of members of a Facet) is called Facet Term. Code assigned to Facet Term (FT) is called Facet Term Code (FTC).

.. _terms-facet-map

   Facet Map
      Pairing of an Item with one or more Facet Terms in one or more Facet Trees.

.. _terms-relation

   Relation (continuing to add precision to the word "Relation" previously used above)
      Line {edge} expressing connection between Facets and Facet Terms in a Graph. Logically, a relation is a verb. Term that describes a Relation is a Predicate.

.. _terms-predicate

   Predicate and Predicate Term
      Type {single} or class {hierarchy} of Relations. A class term (word identifying a collection of Predicate Terms) is called a Predicate. A type term (instances of members of a Predicate Taxonomy) is called Predicate Term. Code assigned to Predicate Term (PT) is called Predicate Term Code (PTC).

.. _terms-syntax

   Syntax (continuing to add precision to the word "Syntax" previously used above, but now specific to Ontology)
      Web Ontology Language (OWL) that specifies the Syntax for creating structures like phrases, sentences, and paragraphs.

.. _terms-grammar-2

   Grammar (continuing to add precision to the word "Grammar" previously used above, but now specific to Ontology)
      Set of statements in the logical form: :class:`subject` :class:`predicate` :class:`object` where :class:`subject` and :class:`object` are Facet Terms and :class:`predicate` are Predicate Terms.

.. _terms-class:

   Class
      Hierarchy of facet terms and/or predicate terms.

.. _terms-relationship:

   Relationship
      Line (edge) expressing connection between facets and facet terms in a graph. Logically, a relationship is a verb.

.. _terms-jointWith:

   jointWith
      TBD

.. _terms-disjointWith:

   disjointWith
      TBD
