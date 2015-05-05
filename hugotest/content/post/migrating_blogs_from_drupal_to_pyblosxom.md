+++
title = "Migrating blogs from Drupal to Pyblosxom"
date = "2010-12-19T19:54:07-04:00"
tags = ["python", "drupal"]
+++
Like many of the modern minimal blog engines it works with plaintext files only (no database), has a relatively small codebase, supports many plugins (like markdown support), is written in a proper scripting language, has a simple and clean file structure, is seo-friendly, and so on.<br />

The one feature that sets it apart from other minimal blog engines is that it supports comments, and doesn't just rely on an external service like disqus, but stores comments as plaintext files as well.<br />

Some features seem a bit overengineered (like, multiple possible locations to store themes (known as "flavours") and templates; I'm a fan of convention over configuration and keeping things simple), but discussing this with the maintainer revealed this is because pyblosxom is meant as a reimplementation of the original perl-based bloxsom project.  Over time features could be simplified and/or redesigned.<br />

So I plan to migrate this blog from drupal to pyblosxom.<br />

To do this, I'm building the tool <a href="https://github.com/Dieterbe/drupal-to-pyblosxom">drupal-to-pyblosxom</a>.<br />

The goal is to convert posts, associated metadata (publish time, tags) and comments from the drupal database to pyblosxom files.  Source code display should be converted too (merely a matter of converting between different plugin conventions), and images shown should be downloaded.  Currently I'm about halfway, if there's anyone out there with a similar use case, help is welcome ;)<!--more--></p>
