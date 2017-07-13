Monkeying around with [Google's Civic Information API](https://developers.google.com/civic-information/docs/v2/). Instructions for obtaining an API Key are [here](https://support.google.com/cloud/answer/6158862).

As a voter, I think it's advantageous to understand, well ahead of any election:

* who represents you at each level of government
* which party they are a member of
* how to call their office

Turns out this is crazy easy to access with this API:

```
$ API_KEY=REDACTED python civic.py "1060 W Addison St, Chicago, IL 60613"
President of the United States:
Donald J. Trump ((202) 456-1111) [Republican]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Vice-President of the United States:
Mike Pence ((202) 456-1111) [Republican]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
United States Senate:
Tammy Duckworth ((202) 224-2854) [Democratic]
Richard J. Durbin ((202) 224-2152) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
United States House of Representatives IL-05:
Mike Quigley ((202) 225-4061) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Governor:
Bruce Rauner ((217) 782-0244) [Republican]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Lieutenant Governor:
Evelyn Sanguinetti ((217) 558-3085) [Republican]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Mayor:
Rahm Emanuel ((312) 744-5000) [Democrat]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
City Clerk:
Anna Valencia ((312) 742-5375) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
City Treasurer:
Kurt Summers ((312) 744-3356) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
State Treasurer:
Michael W. Frerichs ((312) 814-1700) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Attorney General:
Lisa Madigan ((217) 782-1090) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
State Comptroller:
Susana Mendoza ((217) 782-6000) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Secretary of State:
Jesse White ((800) 252-8980) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Sheriff:
Thomas Dart ((312) 603-6444) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Assessor:
Joseph Berrios ((312) 443-7550) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Treasurer:
Maria Pappas ((312) 443-5100) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
County Clerk:
David Orr ((312) 603-5656) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Circuit Clerk:
Dorothy Anne Brown ((312) 603-5030) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
State's Attorney:
Kimberly M. Foxx ((312) 603-1880) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Recorder of Deeds:
Karen A. Yarbrough ((312) 603-5050) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Circuit Court Judge:
Carolyn J. Gallagher (missing) [Democratic]
Aleksandra "Alex" Gillespie (missing) [Democratic]
Susana L. Ortiz (missing) [Democratic]
Brendan A. O'Brien (missing) [Democratic]
Alison C. Conlon (missing) [Democratic]
Mary Kathleen Mchugh (missing) [Democratic]
John Fitzgerald Lyke, Jr. (missing) [Democratic]
Maureen O'Donoghue Hannon (missing) [Democratic]
Patrick Joseph Powers (missing) [Democratic]
Rossana Patricia Fernandez (missing) [Democratic]
Daniel Patrick Duffy (missing) [Democratic]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
County Board President:
Toni Preckwinkle ((312) 603-6400) [Unknown]
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```