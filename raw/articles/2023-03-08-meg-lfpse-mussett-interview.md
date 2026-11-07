---
title: "Lucie Mussett - LFPSE Project Lead at NHS England Breaks Down the New Incident Recording System"
authors: ["Emma Duggan"]
interviewee: "Lucie Mussett (Senior Project Owner and Lead for LFPSE, NHS England)"
publisher: "MEG (megit.com; MEG Support Tools), an LFPSE-compliant quality-management software vendor"
url: "https://megit.com/news-page/lfpse-interview-lucie-mussett"
fetched_url: "https://megsupporttools.squarespace.com/news-page/lfpse-interview-lucie-mussett"
date_published: 2023-03-08
fulltext_source: web-extract
converter: curl + BeautifulSoup (python3 -I) on the post body
notes: |
  Fetched 2026-11-07 from the squarespace URL given in the Dutch report (HTTP 200); the page's canonical
  URL is megit.com/news-page/lfpse-interview-lucie-mussett. schema.org datePublished 2023-03-08T09:38Z,
  dateModified 2023-03-08T10:04Z; author Emma Duggan. The interview is therefore from March 2023, not
  2025-2026. Vendor blog: MEG sells LFPSE-compliant incident-reporting software and says so in the
  standfirst. Full post kept (two standfirst headings, intro, five Q&A sections, ~1,900 words). Left out:
  site navigation, newer/older-post links, office addresses and footer.
---

### In July 2021, NHS England rolled out the national Learn From Patient Safety Events (LFPSE) service — a centralised system that healthcare staff can use to record and access information related to patient safety events nationwide using the NHS database.

### As an LFPSE-compliant vendor , we’re writing a series of blog posts to help healthcare professionals better understand this new incident recording system. If you’d like to know the basics, you can check out our first article: The Five W’s of LFPSE — The New Incident Reporting System in the UK .

As a follow-up, we now deep dive into the LFPSE ecosystem and who better to shed light on the topic than Lucie Mussett, the Senior Project Owner and Lead for LFPSE at NHS England.

With a background in Clinical Policy Management and an MSc in Health Policy from Imperial College London, Lucie has been a part of the National Patient Safety team since 2013. Over the last few years, she has led the agile development team working on LFPSE — the successor to the existing NRLS (National Reporting and Learning System).

We had the privilege to have a conversation with Lucie about the need for LFPSE, what the new system looks like, what’s in store for the future of learning from patient safety events, and more. Take a look at what she had to say!

### What was the need for a new national service for recording patient safety events? What are the key shortcomings of NRLS that LFPSE will be improving on?

Over a decade ago, the National Patient Safety Agency planned to bring the NRLS and StEIS together to streamline the front end and encourage more doctors to report incidents. However, when the Agency was dissolved, that mission was put on hold while responsibilities for patient safety were transferred to the new national patient safety team within the newly formed NHS Commissioning Board, which went on to become NHS England.

When the work restarted, it wasn't just about streamlining NRLS and StEIS anymore. It was more about understanding how healthcare staff are currently using the service and how we'd like them to use it going forward. We wanted to capitalise on the different opportunities that technology brought to the table and do things better to support staff to deliver safer care. In essence, we hoped to create a system that focused on patient safety and a culture of learning from safety events.

The NRLS is a one-of-a-kind, fantastic system with a database of over 20 million reports. However, because it's also on 20-year-old technology, it suffered from stagnating quite a bit in terms of development. While we tried tweaking aspects of the service, particularly around the taxonomy, the infrastructure just didn't allow us to roll out significant changes. There were problems with mapping the different fields to local data structures, technological challenges with getting the data out, and a code limit that wouldn't let us add further features/enhancements to the NRLS.

And so, we decided to take 20 years' worth of learnings from the NRLS system and transpose that into the LFPSE project to build a service that is flexible, accessible, and provides fuller transparency of data. People commit precious time to record safety incidents to support patient safety improvement, but under the NRLS we haven’t always been able to gain the full potential for learning from those records, and there can be a sense they just land in a black box. We recognised that using state of the art technology such as machine learning, would allow us to gain far greater learning and analysis from all recorded incidents. While data in is great and fulfils some needs, data out is where the real capacity for change and learning happens.

### Can you tell us about the LFPSE taxonomy updates, how they'll be used going forward, and how they're going to make things better in terms of data quality?

With respect to taxonomy, we've tweaked and updated the "who, what, where, when, why" data set in LFPSE.

For the "who" question, you can now have multiple patients involved in an event rather than creating separate incident records in the case of events that affect more than one person.

We've updated some categorical data, such as the specialty and service type for the "Where". This allows for more granularity and flexibility, especially when trying to pull out insights from that data. We've also not limited this field to within your organisation — you can record an incident where you think something went wrong when someone else had delivered care earlier in the patient pathway.

Similarly, for "when", we've added the option to estimate the time in cases where people are unaware of the exact time frame. All this is an attempt to improve data quality, provide more flexibility, and not force people into black-and-white answers.

The "what" is where we've made the most significant changes. In the NRLS, there was a finite list of incident types and subtypes, and recorders could only pick one category. This was quite limiting in terms of analysis and learning because incidents are often complicated and cannot be assigned to a single parameter, and the list itself was always incomplete.

Because of this, they would simply be put under the "OTHER" category, where they might get overlooked, because the tendency is to focus on incidents that you already knew were a problem and can be categorised easily. This also means we're missing opportunities to identify under-recognised risks and do more proactive and preventative work, especially in the lower harm categories, which is so essential for safety.

And so, in the LFPSE, we've tried to break down safety events into components. We ask questions about what was physically involved (medications, medical devices, and other tangible aspects), people can multi-select those, and depending on their answers, they see further questions to decipher precisely what went wrong. Some questions go down several levels into finer detail, and others are fairly broad categories.

The final part of the puzzle is the "why", which falls into the world of PSIRF (Patient Safety Incident Response Framework), the new policy replacing the Serious Incident Framework. Under PSIRF, within LFPSE, people can do their reviews, investigations, and exploration of things that have gone wrong and why, and record their learning through the LFPSE front door.

All of this is designed to be updated as and when you have more information — because the records are shared automatically with the national service, there’s no clunky re-uploading with updates: you can just keep tweaking the record as the picture becomes clearer, and we’ll all have sight of that same information as the quality improves.

### What role does Machine Learning play in the information captured nationally? What learnings can be garnered from that data?

A huge amount of work is going on with Machine Learning at the moment, with the potential to really revolutionise how we process data.

We get over 2.6 million records annually; the free text is where all the essential information is. However, at the moment, we only have the capacity to manually read 10,000 a year (usually events classified as severe harm/death in the NRLS). Machine Learning is going to flip that completely. It won't be automating the entire process, but instead identifying keywords, signals, and triggers to sort records that need to be read, in turn, allowing us to do more preventative work.

Machine Learning will also hopefully help us better categorise and tag records and provide healthcare staff recording incidents with tangible feedback and support based on the record created. For instance, if you've recorded a medication incident, the algorithm can quickly scan your record and LFPSE can then send guidance directly to you about preparing and administering the drug in question.

So that is going to address the point raised earlier around people feeling that they take all this time away from their patients, which is where they want to be, to write up this record, and they never see it again, not knowing what good it did and not knowing how to do anything differently. And rather than being a one-sided process, this will create much more of a flow of information, back to the recorders and the recording organisations in a really constructive and helpful way.

### What's in store for the future of LFPSE and patient safety?

We have project plans to tackle different aspects of the system, but with Agile development, you don't really know what you're going to end up with. Our goal with a user-centred design process is not just to refine what we think we need to do but to really listen to our users about what they want and what's going to help them do their job better and more easily.

That being said, we currently have a few different focus areas. Machine Learning is a big one, and so is the Data Access App, which we use to present data back to providers. At the moment, it's only figures, tables, and a few filters, but we're actively working with healthcare staff to explore what tools and data presentations will help them.

We're also looking at improving the capture of protected characteristics information to support our work on addressing inequalities in healthcare and decommissioning the NRLS.

Later in the year, we will be working on a better process to collect patient safety event data from patients and families. Currently, the NRLS has a patient e-form that the patient can fill out. However, that requires the patient to know that what happened to them was a patient safety incident, understand the concept of what patient safety is, and know that there's a team somewhere that they could report it to via an isolated online form; that's a lot of burden on someone who may be unwell.

Our goal is to figure out a better way to include the patient's perspective and contribute to learning without putting that responsibility on the patient.

### What is the role of the different event types (Incident, Risk, Good Care, and Outcomes) in LFPSE?

A mixed bag of stuff always came into the NRLS — sometimes it was risks, other times outcomes or patient safety incidents. However, they were all forced through the same cookie-cutter and had to be reported under a single category: incidents.

For example, if someone were reporting a risk, they would also have to provide a level of harm which was impossible to do because there hadn't been any harm yet. And so, we recognised that people wanted to tell us about different kinds of events and created a system that allowed them to do so — if you're recording a risk, we won't ask for patient details or level of harm because they don't exist. That's the strategy we were going for.

The Good Care workstream is something we're really passionate about. We wanted to focus on not only minimising what goes wrong but also maximising what goes well and learning from it.

At this point, providers must use the "Incident" and "Good Care" event types but have the option to refrain from using "Risk" and "Outcomes". We're keeping those under review, but nobody is obliged to use them. However, if you'd like to use them, we'd love to speak with you for feedback on how it works and if it's useful for staff within your organisation.

We hope there is some benefit in having them, but we need to, as with all of the service, take feedback and find ways to make it user-friendly and work for people.
