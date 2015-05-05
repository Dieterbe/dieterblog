+++
title = "Figuring out CakePHP's new AuthComponent"
date = "2007-04-07T15:52:48-04:00"
tags = ["cakephp", "php", "web2.0"]
+++
<p>However, one of the additions to the 1.2 branch which is currently in active development , is a built-in auth module.  A module that isn't finished yet but it sure is worth it looking at.  (In fact I'm thinking about making a new dAuth version built on cake's own auth system.).  As most bakers know, there is very little information about the 1.2 branch in general, and the auth component in specific.  So what I will try to do, is delve in the code, mess with it, and explain my findings in this post.  <!--more--> For this first post it will be more trying to decipher the source code, messing with it will probably for a little later on.<br />

Disclaimer: not everything I'll say here will be correct, first of all because I'm not able to fully understand every piece of the source code (yet), secondly because the 1.2 api is still changing.</p>

<p>The version i use for this post is svn head. (revision 4758 at time of writing)</p>

<h3>The header</h3>

<p>So let's just open <a href="http://api.cakephp.org/1.2/auth_8php-source.html">cake/libs/controller/components/auth.php</a>.<br />

Reading the first comment we immediately see "Manages user logins and permissions."  This looks very important to me.  Seems like this component handles both authentication and access control.  It seems like the AuthComponent is able to interact with  the <a href="http://manual.cakephp.org/chapter/acl">ACL</a> system that we know from the 1.1 branch.  Multiple uses of the AclComponent ($this->Acl inside the component) confirm this.</p>

<h3>Member variables</h3>

<p>The AuthComponent has quite some member variables, the most important ones seem to me:</p>

<ul>

<li><strong>$userModel</strong> (aro's) &amp; <strong>$objectModel</strong> (aco's)</li>

<li><strong>$loginAction</strong>:  url for login action, null by default but we should set this (to something like 'users/login') when we want to use the component in our application. As usual AppController's beforeFilter() seems like a good place for that.</li>

<li><strong>$validate</strong>:  set to 'actions' or 'objects', depending on what you want to check the access for.  Actually there are more options, read on.  However: on first sight it seems like combinations of objects-actions aren't possible...Anyone knows more about this?</li>

<li><strong>$_loggedIn</strong>:  true/false</li>

<li><strong>$allowedActions</strong>: no user validation on these actions</li>

</ul>

<h3>Functions</h3>

<p>Now, let's move on to the available functions (the most important ones that is) ...</p>

<ul>

<li>

<strong>initialize(&amp;$controller)</strong> seems to be a new ( in 1.2) callback.<br />

Dispatcher calls $controller->_initComponents(), which (controller.php) in turn calls $component->init($this), which calls $tempComponent->initialize($controller).<br />

So this function is called automatically, and when that happens $controller->params are all copied to $this->params (by value).  Some more stuff happens but I don't think it's very important at this time.</li>

<li>The <strong>startup(&amp;$controller)</strong> callback is familiar to 1.1 users.  It is called in the startup-phase of the component, shortly after the initialize callback.  What happens here?

<ul>

<li>The password in $controller->data is hashed by using a call to "Security::hash(CAKE_SESSION_STRING . $password)". (called via $this->hashPasswords() which calls $this->password().<br />

After that $this->data = $controller->data;</li>

<li>A check whether ($this->allowedActions == array('*') || in_array($controller->action, $this->allowedActions)).<br />

In this case no further processing is needed: access is granted, i don't know why we return false here, though</li>

<li>Then we have 2 cases:<br />

Either we are at the login action (defined by $loginAction like mentioned earlier), or we are somewhere else.  I think it will be clear what happens when you study the code, but I do think it's important to mention that the actual login happens at line 274 ($this->login($data), function definition at 470).<br />

The identify function at line 624 is important too.  I guess this one checks the credentials.<br />

If we are somewhere else then $loginAction, access is checked at line 293 (function isAuthorized(), function definition at 332.<br />

Inside this function, $validate is assigned to $type, so it seems like not only 'actions' and 'objects' are valid values, but also 'association' and 'controller'.  I don't really get why this is made so complicated (the __authType() step for example.).</li>

</ul>

</li>

<li>Another callback new in 1.2 is <strong>shutdown(&amp;$controller)</strong>.  Unlike initialize, this one is mentioned on <a href="http://cake.insertdesignhere.com/posts/view/17">Nate's blog</a>.  It removes 'Auth.redirect' from the session when the user is logged in.</li>

</ul>

<h3>Conclusion</h3>

<p>This was only a slight introduction, more research (and thus explanations) will happen later on and you can also expect some sample code.  Give me some time though ;-)</p>
