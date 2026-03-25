# Almedalsdata

Almedalsdata is a small civic tech project I worked with on my free time. The first step was to find as much of the programs as I could online. The second was to write a small script to fetch that data and convert it to a structured format.

You can read more about the project in [English](https://pierre.mesu.re/posts/almedalsdata/) and [Swedish](https://pierre.mesu.re/sv/posts/almedalsdata/).

The generated data is considered an *allmän handling* according to Swedish law. Its license is therefore CC0. The code is licensed with AGPLv3.
Region Gotland doesn't hold any responsibility for the accuracy of the information in the dataset.

## Tech details

As said earlier, the official program website doesn't have any open API. Until 2025, the list was fetched by the website as a JSON containing HTML blocks. I wrote a script that fetches that list by iterating through its pages. It then fetches the information of each event from the event pages. The content is saved both as CSV and JSON.

Since 2025, there is a more modern private API that returns JSON so this project isn't as useful. But it remains as a repository with all the past programs.

## Available years

✅ 2025
✅ 2024
✅ 2023
✅ 2022
✅ 2021
✅ 2020
✅ 2019
✅ 2018
✅ 2017
✅ 2016
✅ 2015
✅ 2014
✅ 2013
✅ 2012
✅ 2011
✅ 2010
✅ 2009
