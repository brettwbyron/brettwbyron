<ul class="list-unstyled flex-row flex-m-space-around flex-c-center">
  <li class="circle-item">
    <a class="circle" href="{{ "/" | relative_url }}">
      <i class="fa fa-home"></i>
    </a>
    <p>Home</p>
  </li>
  <li class="circle-item">
    <a class="circle" href="{{ "/code" | relative_url }}">
      <i class="fa fa-code"></i>
    </a>
    <p>Code</p>
  </li>
  <li class="circle-item">
    <a class="circle" href="{{ "/config" | relative_url }}">
      <i class="fa fa-cog"></i>
    </a>
    <p>Config</p>
  </li>
</ul>

# Getting Git Installed
### Mac
If you're not sure if you have Git installed already:
1. Open ```Terminal.app```
2. In the terminal, type ```git --version```
3. If there is a number there, it's installed! If there isn't go to [this link](https://git-scm.com/download/mac) and install.

### Windows
If you're not sure if you have Git installed already:
1. Open `Command Prompt.exe`
2. In the terminal, type `git --version`
3. If there is a number there, it's installed! If there isn't go to [this link](https://git-scm.com/download/win) and install.

## Ways to interact with Git
If you're not ready to, or don't want to, work in the terminal here are GUIs (**G**raphic **U**ser **I**nterfaces) for Git. Here are a few:
1. GitHub [Mac](https://mac.github.com/) [Windows](https://windows.github.com/)
2. GitKraken [Download](https://www.gitkraken.com/download)
3. Sourcetree [Download](https://www.sourcetreeapp.com/)

# Setting Up Git

If you don't have a **work** Git account, create one with your work email address.

#### Getting your computer ready for your work with Git.
1. Create a base folder in your `Documents` folder and name it `CWS`. This is where you want to keep all of your work.
2. Clone this repo! (type `git clone https://github.com/brettwbyron-jobvite/CWS.git` in your terminal or clone via your chosen GUI using this Git clone URL https://github.com/brettwbyron-jobvite/CWS.git)
3. Add all of your existing project folders into your new `CWS` folder.
3. Through your terminal or GUI, create a new branch and name it `your-name-here`. This will be your "final draft" branch; where you put your finished work.

# Working with branches
When working on a project, the changes you make to one project shouldn't risk putting other projects in harms way (everyone makes mistakes!). How to make sure that doesn't happen is to create a new branch for the project you're working on. Here's an example:

### Example
Files/Folders:
```
- /
-- Foo
  --- style
    ---- desktop.css
    ---- mobile.css
  --- joblisting.html
  --- images
    ---- image1.jpg
-- Bar
  --- style
    ---- desktop.css
  --- index.html
```
##### Creating Branches
Let's say I am going to be working on project Foo. To set myself up, I need to create a new branch (if one isn't created already) for this project. What I'm going to do, is create a branch and naming it with the same name as the project. If I'm using the terminal, I need to type the following:
```
git branch foo  // this creates a branch 'foo'
```
<p id="crap-gui" class="anchor">If I'm using a GUI, there should be a clear option to create a branch. If there isn't a clear option, then I should probably <a href="https://www.google.com/search?&q=git+gui" target="_blank" rel="noopener">ask Google</a> or look for a new GUI (some GUIs aren't great).</p>

##### Checking Out of Branches
Now that my branch is created, I need to make sure I'm working in it! In order to switch branches, I need to make sure I don't have any changes in my current branch. To check if I have any changes in my current branch and I'm using the terminal, I just need to type:
```
git status
```
This will show me all the changes in my files, if there are any.

If I'm using a GUI, it should be clear to see if there are changes in the files in your current branch. If it isn't clear and causes issues, [follow the directions above about not great GUIs](#crap-gui).

_In this example, let's assume that I have no changes._

Now that I know I don't have any changes in my current branch, I'm going to checkout to the new branch. If I'm using the terminal, I need to type the following:
```
git checkout foo
```
If I'm using a GUI, I should be able to click/double-click between branches to checkout and change branches.

So, I've created my branch (WOOT!) and now I can start working on my Foo project. Now that I'm working on some stuff, I want to save my work. To do this, I need to stage my work, commit my changes, and push my code.

##### Committing / Pushing
To save my changes, I need to do a few things in order to **commit** the changes I've made. First, I need to add/stage the files that are changed. If I'm using the terminal, I need to type the following:
```
git add .  // this adds ALL changed files
// OR
git add filename.extension // this adds the changed filename.extension file
```
If I'm using a GUI, there should be a clear option to "Stage" or "Add" files to a commit. If there isn't a clear option, [follow the directions above about not great GUIs](#crap-gui).

Second, now that my changes have been staged, I need to **commit** these files and prepare to **push** these changes to my branch. If I'm using the terminal I need to type the following:
```
git commit -m "This is a message I need to write to describe my changes to these files."
```
If I'm using a GUI, there should be a clear option to write a message and commit my changes. If there isn't a clear option, [follow the directions above about not great GUIs](#crap-gui).

Third, now that my changes have been staged and I have committed them, it's time to **push**! Pushing to my branch means that my changes will now be saved and I'll be able to see those changes in Git and see the files I changed and the lines of code I changed (sweeeeeet)! So, if I'm using the terminal I need to type the following:

If it is my very first push to this branch, I'm going to need to set my upload stream to the original (**origin**) branch on the server from my remote branch on my computer. So, if I'm using the terminal, I need to type the following:
```
git push --set-upstream origin branch-name
```
If I'm using a GUI, I probably won't need to worry about this.
If it isn't my first push to this branch and I'm using the terminal, I just need to type `git push` because my upload stream is already set.

Done! I have successfully created a branch, staged my changes, commited those changes with a message, and pushed those changes to my branch! Yay!


This repo is for all career site folders. (like our current ftp 'uploads' folder)
If there are questions, [ping me](https://jobvite.slack.com/team/brett.byron){:target="_blank" rel="noopener"}!
