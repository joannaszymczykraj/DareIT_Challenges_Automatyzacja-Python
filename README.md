# Portfolio - Joanna Szymczyk-Raj  <p> :sparkles: Dare IT Challenges Testy Automatyczne + Python :sparkles: </p>

### :loop: Table of contents <p></p>

* :eight_spoked_asterisk: <b>[Task 1: The Software configuration](#task-1-the-software-configuration)</b> <p></p>
* [Subtask 1: Why did I decided take part in Dare IT Challenge project?](#subtask-1-why-did-i-decided-take-part-in-dare-it-challenge-project)
* [Subtask 2: Repairing a problem on the console](#subtask-2-repairing-a-problem-on-the-console)
* [Subtask 3: Adding a code to my repository](#subtask-3-adding-a-code-to-my-repository)
* [Subtask 4: Special task - purpule test](#subtask-4-special-task---purpule-test) <p></p>
* :eight_spoked_asterisk: <b>[Task 2: Selectors](#task-2-selectors) </b><p></p>
* [Subtask 1: Special task - new branch](#subtask-1-special-task---new-branch)
* [Subtask 2: Searching for selectors on the login page. Show all items from the login page](#subtask-2-searching-for-selectors-on-the-login-page-show-all-items-from-the-login-page)
* [Subtask 3: Adding selectors to the project](#subtask-3-adding-selectors-to-the-project)
* [Subtask 4: Adding a new field to the project](#subtask-4-adding-a-new-field-to-the-project)
* [Subtask 5: Addind a new field - add a match form](#subtask-5-addind-a-new-field---add-a-match-form)
* [Subtask 6: Special task - branch merging](#subtask-6-special-task---branch-merging) <p></p>
* :eight_spoked_asterisk: <b>[Task 3: First test case and assertion](#task-3-first-test-case-and-assertion) </b><p></p>
* [Subtask 1: Completing the login page](#subtask-1-completing-the-login-page)
* [Subtask 2: New test case](#subtask-2-new-test-case)
* [Subtask 3: Assertion](#subtask-3-assertion)
* [Subtask 4: Repeating](#subtask-4-repeating) <p></p>
:eight_spoked_asterisk: <b>[Task 4: Refactor, debugger and test cases](#task-4-refactor-debugger-and-test-cases) <b/><p></p>
:eight_spoked_asterisk: <b>[Task 5: Robot framework](#task-5-robot-framework) <b/><p></p>
:eight_spoked_asterisk: <b>[Task 6: Bug report, test report and portfolio](#task-6-bug-report-test-report-and-portfolio) <b/>

   <p></p>
  <p></p>

__________________________________________________________
  
## Task 1: The Software configuration <p></p>
__________________________________________________________
### Subtask 1: Why did I decided take part in Dare IT Challenge project?
<details>
<summary>Click here to see general information about <b>Subtask 1</b></summary>
At the beginning of 2023, I decided to change the industry. The choice fell on a software tester. I started self-study, got the <b>ISTQB certificate</b> and participated in several testing congresses (for example <b>Test:Fest</b>). I really feel like doing this and it's my objective for this year. A few months ago I took part in the <b>Manual Tester Challenge</b> project. I decided that the course was very valuable and taking into account the situation on the testing job market, I decided that participation in the Introduction to Automated Testing + Python Challenge would be a good step. I hope that I will learn new things, broaden my horizons, gain experience necessary to apply for my first job as a software tester.
</details>

### Subtask 2: Repairing a problem on the console
<details>
<summary>Click here to see general information about <b>Subtask 2</b></summary>
Fortunately, I don't get this error (or I don't see it :sweat_smile:) So I'm going to the next task.
</details>

### Subtask 3: Adding a code to my repository
<details>
<summary>Click here to see general information about <b>Subtask 3</b></summary>
The code added. Files moved to the repository.
</details>

### Subtask 4: Special task - purpule test
<details>
<summary>Click here to see general information about <b>Subtask 4</b></summary>
My test result: 13/14
</details>

__________________________________________________________
## Task 2: Selectors
__________________________________________________________

### Subtask 1: Special task - new branch
New branch "selectors" added to PYcharm.

### Subtask 2: Searching for selectors on the login page. Show all items from the login page
<details> 
<summary><b>1.	HEADER_SCOUTS_PANEL_XPATH</b></summary>
  
<div>
 <p>
   <b>copy XPath= //*[@id="__next"]/form/div/div[1]/h5</b>
 </p>

<p>
  <ol> 
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/h5[1]</li>
  <li>//h5[contains(@class,'gutterBottom')]</li>
  <li>//h5[@class='MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom']</li>
  </ol>
</p>
</div>
</details>

<details> 
<summary><b>2. LOGIN_XPATH</b></summary>

<div>
  <p>
<ul><b>a) Login_field_xpath</b></ul>
  </p>
 <b>copy XPath= //*[@id="login"]</b>
<p>
  <ol>
    <li>//input[contains(@class,'MuiInputBase') and @name='login']</li>
    <li>//input[@name='login']</li>
    <li>//input[starts-with(@class,'MuiIn')]</li>
    <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]</li>
  </ol>  
</p>

<ul><b>b) Login_label_xpath</b></ul>

<b>copy XPath= //*[@id="login-label"]</b>
<p>
<ol>
  <li>//label[text()='Login']</li>
  <li>//label[@id='login-label']</li>
  <li>//label[contains(@class,'MuiFormLabel-') and @id='login-label']</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/label[1]</li>
</ol>
</p>
</div>
</details>



<details> 
<summary><b>3. PASSWORD_XPATH</b></summary>

<div>
 <p>
<ul><b>a) Password_field_xpath</b></ul>
</p> 
<b>copy XPath= //*[@id="password"]</b>
  <p>
<ol>
  <li>//input[@id='login']</li>
  <li>//input[contains(@class,'MuiInputBase') and @name='login']</li>
  <li>//input[starts-with(@name,'log')]</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/input[1]</li>
</ol>
</p>

<ul><b>b) Password_label_xpath</b></ul>
<p>
<b>copy XPath= //*[@id="password-label"]</b>
  </p>
  <p>
<ol>
  <li>//label[@id=’password-label’]</li>
  <li>//label[text()='Password']</li>
  <li>//label[contains(@class,'formControl') and @for='password']</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[1]/div[2]/label[1]</li>
</ol>
</p>
</div>
</details>


<details>
  <summary><b>4. REMINDER_PASSWORD_LABEL_XPATH</b></summary>

<div>
  <p>
<b>copy XPath= //*[@id="__next"]/form/div/div[1]/a</b>
</p>
  <p>
<ol>
  <li>//a[text()='Remind password']</li>
  <li>//a[contains(@class,'MuiLink-root')]</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]</li>
  <li>//a[@tabindex='-1']</li>
</ol>
  </p>
</div>
</details>



<details>
<summary><b>5.	LANGUAGE_CHANGE_BUTTON_XPATH</b></summary>
  
<div>
  <p>
<b>copy XPath= //*[@id="__next"]/form/div/div[2]/div/div</b>
 </p>
  <p>
<ol>
  <li>//div[contains(@class,'MuiSelect')]</li>
  <li>//div[text()='English']</li>
  <li>//div[@tabindex='0' and @role='button']</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]</li>
</ol>
  </p>
</div>
</details>


<details>
<summary><b>6.	SING_IN_BUTTON_XPATH</b></summary>
 
<div>
  <p>
<b>copy XPath= //*[@id="__next"]/form/div/div[2]/button/span[1]</b>
 </p>
  <p>
<ol>
  <li>//span[text()='Sign in']</li>
  <li>//span[@class='MuiButton-label']</li>
  <li>//span[contains(@class,'MuiButton')]</li>
  <li>/html[1]/body[1]/div[1]/form[1]/div[1]/div[2]/button[1]/span[1]</li>
</ol>
  </p>
</div>
</details>

### Subtask 3: Adding selectors to the project
Job done - selektors added to the projekt in the login_page tab in PyCharm.

### Subtask 4: Adding a new field to the project
Job done - a new field "dashboard" added to the project in PyCharm.

### Subtask 5: Addind a new field - add a match form
Job done - a new field "add_a_match_form" added to the projekt in PyCharm. Moreover, more than 10 selectors have been added.

### Subtask 6: Special task - branch merging
Job done - merge pull request :muscle:

__________________________________________________________

## Task 3: First test case and assertion

__________________________________________________________

### Subtask 1: Completing the login page
Job done - the login page has been completed.
### Subtask 2: New test case
Job done - the new test case has been done. 
### Subtask 3: Assertion
Job done - the assertion has been done.
### Subtask 4: Repeating
<details>
<summary>Click here to see general information about <b>Subtask 4</b></summary>
 <p>
   <div>
   <b>Tasks done:</b></p>
    <p>
    <ol>
    <li>creation a new page</li>
    <li>creation a new test case</li>
    <li>use an assertion method</li>
    </ol>
    </p>
   </div>
  <p>
  Job done - I'm a master :superhero_woman: :laughing:
</p>
   </details>  

__________________________________________________________

## Task 4: Refactor, debugger and test cases

__________________________________________________________

<details>
<summary>Click here to see general information about <b>Task 4 </b></summary>
 <p></p>
  
I must admit that this task turned out to be very difficult for me. Mainly because the tests from task 3 that I was getting have (and I was very proud of it!), now stopped working. Sometimes they worked, sometimes they didn't. It took me a long time to grasp this topic. Real blood, sweat and tears. And little sleep.
But it works for me ;-)
Task 4, after researching task 3 in depth, somehow went. I have killer timings in TC, but I think the cause of my problems is a weak computer :-D
I hope my codes will work for you too!

And the end I have to say that it was really fun to sit at night and look for bugs in my own code with bated breath. This is great! But I don't have the strength (and time) for additional tasks... Forgive me

:point_right:Link to my <b>Google Drive</b>: https://drive.google.com/drive/folders/15N5ag82py6HUjEIwgRqGIMbfVKt_8F6s?usp=drive_link

   </details>

__________________________________________________________
## Task 5: Robot framework

__________________________________________________________

<p></p>
:point_right:Link to my new repository with <b>robot framework<b>: https://github.com/joannaszymczykraj/panelscouts_robotframework.git

__________________________________________________________
## Task 6: Bug report, test report and portfolio

__________________________________________________________
<p></p>
:point_right: Link to my <b>Google Drive with Task 6<b>: https://drive.google.com/drive/folders/16v1R3lYfInhQ_OqfTN5G1MDHr3qYxFy2?usp=drive_link
<p></p>
:point_right: Link to my <b>Portfolio<b>: https://github.com/joannaszymczykraj/Portfolio_J_Szymczyk-Raj/blob/main/README.md
