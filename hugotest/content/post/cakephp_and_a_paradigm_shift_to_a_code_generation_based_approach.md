+++
title = "CakePHP and a paradigm shift to a code generation based approach?"
date = "2009-01-19T22:16:52-04:00"
tags = ["foss", "cakephp"]
+++
<p>At my <a href="/jobhunt_over">new job</a>, I'm writing a quite full-featured web application.<br />

I've choosen to use CakePHP.<br />

Why? Well, it may be 2 years since I last used it, but I've followed the project and it's planet, and it seems to have matured and gained even more monumentum.<br />

I want to use something that is widely used so there is plenty of stuff available for it, it's RAD, it's flexible and powerful.<br />

I noticed things such as CLI support and documentation have improved tremendously too.</p>

<p>However, I find that still, the recommended (or at least "most commonly used") practices are not as efficient as they could be, and that emphasis is placed on the wrong aspects.<br />

See, even though the <a href="http://book.cakephp.org/view/113/Code-Generation-with-Bake">bake</a> tool has come a long way since I last used it, it's still used to "generate some standard models/controllers/views" and the developer can take it from there [further editing the resulting files himself].<br />

Finetuning generated code by editing the templates (in fact, only views have templates; the php code of models and controllers is hardcoded in the scripts that generate them), is still an obscure practice...<br />

Also, there are very few commandline switches (Right now you can choose your app dir, whether you want to bake a model,controller or view, and it's name.)<br />

All other things (validation rules, associatons, index/view/edit/add actions/views, which components, overwrite yes/no etc) are all handled interactively.<br />

There are also some smaller enoyances such as when you specify one option like the name of the model, it assumes you don't want interactivity and produces a model containing nothing more then the class definition and the membervariable $name, which is usually worthless.<br />

One thing that is pretty neat though, If you update $this->recursive in a model, the baked views will contain stuff for the associated things.  But so much more could be done...<br />

<!--more--></p>

<p>Ideallistically speaking, the bake tool (and it libraries) should imho become much more advanced:</p>

<ul>

<li>templates for views, models and controllers.</li>

<li>choice of multiple (groups of) templates which you can choose with a commandline argument. (eg I typically have some different kinds of M/V/C's for a certain model, but there are many similarities and they can often even be categorised into groups.)</li>

<li>the ability to control all aspects of the bake process through commandline switches (or config files).  Both the things that are asked now but also $recursive level, behaviors you want to use for models, etc.</li>

<li>proper cmdline arg parsing (getline or something)</li>

</ul>

<p>We could then do a paradigm shift to actually treat your models, views and controllers as uncritical "output" code which can be deterministically regenerated (and hence doesn't need to be versionned), while the templates and the scripts to call bake become your "source", and your key asset to building the application you're working on.</p>

<p>If I had the time (or would use cake for personal projects) I would happily work on such refactorings in a clean way.<br />

For now though,  I've hacked/workarounded/patched the cake code in such a way that it behaves the way I want, while spending as little time on it as possible.<br />

For those interested, the patched code is online at <a href="http://github.com/Dieterbe/cake/tree/master" title="http://github.com/Dieterbe/cake/tree/master">http://github.com/Dieterbe/cake/tree/master</a><br />

The first rev is the original cakephp code, so you can look at the diffs if you want.</p>

<p>Changes until now ( <a href="http://github.com/Dieterbe/cake/commit/9ceb6234164ebc750c8b697a825834ca36097ce7" title="http://github.com/Dieterbe/cake/commit/9ceb6234164ebc750c8b697a825834ca36097ce7">http://github.com/Dieterbe/cake/commit/9ceb6234164ebc750c8b697a825834ca3...</a> ):</p>

<ul>

<li>Do not clear my terminal. (why is that needed anyway :/)</li>

<li>Some echo's that tell me which shells are loaded, tasks executed etc (to understand more how it all works)</li>

<li>always overwrite files.  Hey I use version control!  always bake unit tests, always bake all actions/views, except those for admin routing</li>

<li>never ask me which db to connect to, never use scaffolding, don't use helpers, don't write $useDbConfig to models (it's loaded dynamically in app_model),</li>

<li>agree with all associations except the hasOne's (I can build in exceptions/specific rules if I ever need them)</li>

<li>validation rules are specified as sql comments.  I don't want to re-answer those questions each time I rebake.</li>

</ul>

See this example sql file.  When baking a model, the code will first try to find a specific rule for the model, if not found, it will look for a global rule, and if still not found, ask the question interactively.<br />

[code lang="sql"]<br />

-- cake validate ALL id none<br />

-- cake validate ALL created none<br />

-- cake validate ALL modified none<br />

(...)<br />

CREATE TABLE foos (<br />

    id serial NOT NULL,<br />

    name character varying(255) NOT NULL, --cake validate apc alphanumeric<br />

    type character varying(255) NOT NULL, --cake validate apc notempty<br />

    room_id integer NOT NULL, --cake validate apc numeric<br />

    created timestamp without time zone,<br />

    modified timestamp without time zone<br />

);<br />

[/code]

</ul>

<p>Here is the bash code which I currently use to bake all my models without any interactivity:</p>

<p>[code lang="bash"]<br />

for i in `cake bake model <<< 'q' | awk '/^[[:digit:]]/ {print $2}'` #get a list of all models<br />

do<br />

        if [ $i != Aro ] &amp;& [ $i != Aco ] &amp;& [ $i != ArosAco ]<br />

        then<br />

                echo ">>> doing $i...."<br />

                cake bake model $i<br />

        fi<br />

done<br />

[/code]</p>

<p>I may post later again about this stuff if I have something useful to say.</p>
