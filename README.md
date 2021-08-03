# Almedalsdata
Almedalsdata is a small civic tech project I worked with on my free time. The first step was to find as much of the programs as I could online. The second was to write a small script to fetch that data and convert it to a structure format.

You can read more about the project [here](https://medium.com/civictechsweden/almedalsdata-diving-into-the-data-of-the-worlds-biggest-political-festival-267eb6865860).

## Tech details

As said earlier, the official program website doesn't have any open API, or barely, the list is fetched by the website as a JSON containing HTML blocks. 🤦🏻‍♂️.

I wrote a script that fetches that list by iterating through its pages. It then fetches the information of each event from the event pages.

The content is saved both as CSV and JSON.
## Roadmap

✅ 2021 ([link](https://program.almedalsveckan.info/event/list/2021))
✅ 2020 (Only available through [API](https://program.almedalsveckan.info/event/search/events/2020/seminar/0))
✅ 2019 (Only available through [API](https://program.almedalsveckan.info/event/search/events/2019/seminar/0))
✅ 2018 (Only available through [API](https://program.almedalsveckan.info/event/search/events/2018/seminar/0))
✅ 2017 ([link](https://program.almedalsveckan.info/event/list/2017))
✅ 2016 ([link](https://program.almedalsveckan.info/event/list/2016))
✅ 2015 ([link](https://program.almedalsveckan.info/event/list/2015))
✅ 2014 ([link](https://program.almedalsveckan.info/event/list/2014))
✅ 2013 ([link](https://program.almedalsveckan.info/event/list/2013))
✅ 2012 ([link](https://program.almedalsveckan.info/event/list/2012))
✅ 2011 ([link](https://program.almedalsveckan.info/event/list/2011))
✅ 2010 ([link](https://program.almedalsveckan.info/event/list/2010))
✅ 2009 ([link](https://program.almedalsveckan.info/event/list/2009))
✅ 2009 ([link](https://program.almedalsveckan.info/event/list/2009))
❌ 2008 ([link](https://program.almedalsveckan.info/event/list/2008))
❌ 2007 ([link](https://program.almedalsveckan.info/event/list/2007))
❌ 2006 ([link](https://program.almedalsveckan.info/event/list/2006))
❌ 2005 ([link](https://program.almedalsveckan.info/event/list/2005))
❌ 2004 ([link](https://program.almedalsveckan.info/event/list/2004))
❌ 2003 ([link](https://program.almedalsveckan.info/event/list/2003))
...

The last years marked in red are only partly available and in an older format so they haven't been added yet. Any year older than 2003 isn't even available online (to my knowledge).
