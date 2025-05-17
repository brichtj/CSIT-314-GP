<template>
  <div>
    <h2>Posts per Day</h2>
    <Chart
      v-if="dailyData.length"
      type="line"
      :data="dailyChartData"
      :options="chartOptions('Date')"
    />
    <p v-else>No daily data available.</p>

    <h2>Posts per Week</h2>
    <Chart
      v-if="weeklyData.length"
      type="line"
      :data="weeklyChartData"
      :options="chartOptions('Week Start')"
    />
    <p v-else>No weekly data available.</p>

    <h2>Posts per Month</h2>
    <Chart
      v-if="monthlyData.length"
      type="line"
      :data="monthlyChartData"
      :options="chartOptions('Month Start')"
    />
    <p v-else>No monthly data available.</p>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useManagementStore } from '@/stores/management'
import type { ReportEntry } from '@/types/interfaces'

const managementStore = useManagementStore()

// Helper: parse ISO date string -> Date
const parseDate = (d: string) => new Date(d + 'T00:00:00')

// Helper: format Date -> ISO string 'YYYY-MM-DD'
function formatDate(d: Date): string {
  const year = d.getFullYear()
  const month = String(d.getMonth() + 1).padStart(2, '0') // month 0-11
  const day = String(d.getDate()).padStart(2, '0')
  return `${year}-${month}-${day}`
}

// Generate all dates between start and end inclusive (daily)
function fillMissingDays(data: ReportEntry[]): ReportEntry[] {
  if (!data.length) return []

  const sorted = data
    .slice()
    .sort((a, b) => parseDate(a.date).getTime() - parseDate(b.date).getTime())
  const start = parseDate(sorted[0].date)
  const end = parseDate(sorted[sorted.length - 1].date)

  const result: ReportEntry[] = []
  for (let dt = new Date(start); dt <= end; dt.setDate(dt.getDate() + 1)) {
    const iso = formatDate(dt)
    const found = data.find((d) => d.date === iso)
    result.push(found ?? { date: iso, postcount: 0 })
  }
  return result
}

// Generate all weeks between start and end inclusive
function fillMissingWeeks(data: ReportEntry[]): ReportEntry[] {
  if (!data.length) return []

  const sorted = data
    .slice()
    .sort((a, b) => parseDate(a.date).getTime() - parseDate(b.date).getTime())
  let start = parseDate(sorted[0].date)
  let end = parseDate(sorted[sorted.length - 1].date)
  console.log(start, end)

  // normalize start to the Monday of that week (or Sunday depending on your week start)
  start.setDate(start.getDate() - ((start.getDay() + 6) % 7))
  console.log(start)
  console.log(formatDate(start))
  console.log(data[0].date)
  const result: ReportEntry[] = []
  for (let dt = new Date(start); dt <= end; dt.setDate(dt.getDate() + 7)) {
    const iso = formatDate(dt)
    const found = data.find((d) => d.date === iso)
    result.push(found ?? { date: iso, postcount: 0 })
  }
  return result
}

// Generate all months between start and end inclusive
function fillMissingMonths(data: ReportEntry[]): ReportEntry[] {
  if (!data.length) return []

  const sorted = data
    .slice()
    .sort((a, b) => parseDate(a.date).getTime() - parseDate(b.date).getTime())
  let start = parseDate(sorted[0].date)
  let end = parseDate(sorted[sorted.length - 1].date)

  start = new Date(start.getFullYear(), start.getMonth(), 1)
  end = new Date(end.getFullYear(), end.getMonth(), 1)

  const result: ReportEntry[] = []
  for (let dt = new Date(start); dt <= end; dt.setMonth(dt.getMonth() + 1)) {
    const iso = dt.toISOString().slice(0, 7) + '-01' // e.g. '2023-05-01'
    const found = data.find((d) => d.date === iso)
    result.push(found ?? { date: iso, postcount: 0 })
  }
  return result
}

// Usage example with your refs:
const dailyData = ref<ReportEntry[]>([])
const weeklyData = ref<ReportEntry[]>([])
const monthlyData = ref<ReportEntry[]>([])

// After fetching raw data from backend:
async function loadData() {
  const rawDaily = await managementStore.getReport('daily')
  dailyData.value = fillMissingDays(rawDaily)

  const rawWeekly = await managementStore.getReport('weekly')
  weeklyData.value = fillMissingWeeks(rawWeekly)

  const rawMonthly = await managementStore.getReport('monthly')
  monthlyData.value = fillMissingMonths(rawMonthly)
}

// Chart option generator
const chartOptions = (xLabel: string) => ({
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
  },
  scales: {
    x: {
      title: {
        display: true,
        text: xLabel,
      },
    },
    y: {
      title: {
        display: true,
        text: 'Post Count',
      },
      beginAtZero: true,
    },
  },
})

// Chart data for each chart
const dailyChartData = computed(() => ({
  labels: dailyData.value.map((entry) => entry.date),
  datasets: [
    {
      label: 'Posts per Day',
      data: dailyData.value.map((entry) => entry.postcount),
      borderColor: '#42A5F5',
      fill: false,
      tension: 0.4,
    },
  ],
}))

const weeklyChartData = computed(() => ({
  labels: weeklyData.value.map((entry) => entry.date),
  datasets: [
    {
      label: 'Posts per Week',
      data: weeklyData.value.map((entry) => entry.postcount),
      borderColor: '#66BB6A',
      fill: false,
      tension: 0.4,
    },
  ],
}))

const monthlyChartData = computed(() => ({
  labels: monthlyData.value.map((entry) => entry.date),
  datasets: [
    {
      label: 'Posts per Month',
      data: monthlyData.value.map((entry) => entry.postcount),
      borderColor: '#FFA726',
      fill: false,
      tension: 0.4,
    },
  ],
}))

// Load all reports when component mounts
onMounted(async () => {
  loadData()
})
</script>
