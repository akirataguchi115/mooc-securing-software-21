## LINK:

https://github.com/akirataguchi115/mooc-securing-software-21/project-1

`python manage.py runserver` starts the server in http://localhost:8000. Simple tasks can be added. For admin panel navigate to http://localhost:8000/admin/login/?next=/admin/ though one probably won't have the password for the panel.

## FLAW 1: A01:2021 - Broken Access Control

https://github.com/akirataguchi115/mooc-securing-software-21/blob/main/project-1/server/pages/views.py#L7-L11

The function changeUsernameView can be accessed from /change which is defined in the urls.py. This would be somewhat fine on it's own security wise but any currently any non-logged-in user can access this url and trigger the admin password change.

In A01:2021 this is also known as "Accessing API with missing access controls-".

To fix this issue one should add @login_required decorator to the view definition. There are also other decorators and other methods that would prevent unwanted users with more options.
## FLAW 2: A04:2021 - Insecure design

https://github.com/akirataguchi115/mooc-securing-software-21/blob/main/project-1/static/js/script.js#L21

Static javascript assets can be manipulated during runtime of the web software. For example one could just change the if clause to True entirely and print out to the secret message for admins only regardless of the conditions. It's no wonder that A04:2021 is the fourth biggest problem in cyber security currently. It is somewhat of a trade-off to verify the same data all over again in different layers. Trade-off or not this is insecure design.

To prevent this kind of vulnerability one should follow the general workflow that the bigger frameworks such as Django offers. For example Django does not directly support serving static files in production mode. This particular vulnerability can easily be fixed by doing the validation pythonside and on the server rather than on the client.

## FLAW 3: A06:2021 - Vulnerable and Outdated components

https://github.com/akirataguchi115/mooc-securing-software-21/tree/main/project-1/requirements.txt

There are no dependencies whatsoever listed in the application. It is entirely on the responsibility of the other developer to install needed dependencies. This could lead to installing vulnerable and outdated components. With python this is more than likely as the components can be installed beforehand and without any virtual environment. Not only is this unsafe it is a software-breaking design. This software is implemented with static configurations of Django 3.2 in mind yet the newest Django 4.0 uses different syntax in pointing the static files location. This is the best case scenario where the outdated component just stops working whereas the worst case scenario is the software working and allowing the vulnerable components live rent-free for an arbitrary period of time.

To fix this issue one should either pip freeze the requirements to a file and make the instructions to installing the dependencies into a virtual environment and running the application as intended. Another solution would be to use the listvulnerability.py scanner with pip list or the frozen requirements to check for any vulnerabilities and deprecations. All of this could be taken one step further by using some package management tool of sorts so that there would be even less room for error. One could use Docker to make the whole environment setup itself abstract so that no error could be made. Just like with actual security the list goes on and on as the nature of cyber security is and probably always will be about making the software more secure though never fully secure.

## FLAW 4: A07:2021 - Identification and Authentication Failures

https://github.com/akirataguchi115/mooc-securing-software-21/blob/main/project-1/server/db.sql#L127

Although the password is sha256-encrypted the username is admin which again "Permits automated attacks such as credential stuffing, where the attacker has a list of valid usernames and passwords." This can be proven by using the hackpassword.py with the help of candidates.txt which brute-forces the password succesfully with the help of Django's webtools. With the ever-increasing amount of non-standardized IoT devices it is no wonder Identification and Authentication Failures are still the top 7 issues in cyber security.

To fix this issue one one should not probably not use the admin username in the first place because that would be the first username targeted for password brute-forcing. Making the password longer and non-general also increases the brute-forcing time effectively and making a dictionary attack useless against it. It's also good to note that creating definite password for admin account (or any account for that matter) inside database schemas is not wise. Instead one should create and update the password inside the application's own interfaces. This would also give more flexibility to choosing who can do this and in which conditions. Input validation becomes available also with this method instead of hard-coding credentials.

## FLAW 5: Security Logging and Monitoring Failures

https://github.com/akirataguchi115/mooc-securing-software-21/blob/main/project-1/static/js/script.js#L27

When something goes wrong in the application's task form the software spits out sensitive information to the console of the browser. This is terms that "Auditable events, such as logins, failed logins, and high-value transactions, are not logged." Poorly implemented event logging inside application exposes the inner infrastructure of the software to a possible attacker. Absence of event logging however fails to notify the administrators of possible attacks that have already happened.

To fix the specific issue in this software one could temporarily log the error message to serverside rather than clientside. For example this could be achieved with Python's print() instead of Javascript's console.log(). However the most robust solution to this would be to use an actual event logging middleware software. These too can be vulnerable so it gives us yet another surface to protect from the attackers. A fresh example of this is Log4j vulnerability that has been exploited since 1st of December 2021.