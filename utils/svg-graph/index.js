import { DOMImplementation, XMLSerializer } from 'xmldom';
import { stats } from './dayStats.js';
import Graph from './svg/Graph.js';
import { oneYearPlus } from './svg/utils.js';
import fs from "node:fs"

function generate(start, data = []) {
  const xmlSerializer = new XMLSerializer();
  const document = new DOMImplementation().createDocument('http://www.w3.org/1999/xhtml', 'html', null);

  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  const startDate = new Date(start)
  const endDate = oneYearPlus(startDate)
  const graph = Graph(document, svg, {
    data,
    startDate: startDate,
    endDate: endDate,
  });

  const xml = xmlSerializer.serializeToString(graph);
  return xml
}

const dates = [
  '2023-04-15', '2024-04-15', '2025-04-15'
]

for (const s of dates) {
  const startDate = new Date(s)
  const endDate = oneYearPlus(new Date(s))
  const data = stats(startDate, endDate, (line) => ({ 
    date: line.date, 
    count: line.weight,
    dayNum: line.daynum,
  }))
  // show the stats on hover
  const svg = generate(s, data)
  // console.log(svg)
  // const svg = generate('2024-04-15', data)
  // console.log(svg)
  fs.writeFile(`../../progress-chart${s}.svg`, svg, err => {
    if (err) {
      console.error(err);
    }
  });
}

