import React from "react";
import { Line } from "react-chartjs-2";

const LineChart = ({ chartData, title, xLabel, yLabel }) => {
  const dates = Object.keys(chartData);
  const amounts = Object.values(chartData);

  const options = {
    responsive: true,
    legend: {
      display: false,
    },
    tooltips: {
      callbacks: {
        label: function (tooltipItem, data) {
          const value = tooltipItem.yLabel || 0;
          return value.toLocaleString("vi-VN", {
            style: "currency",
            currency: "VND",
            minimumFractionDigits: 0,
          });
        },
      },
    },
    scales: {
      xAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: xLabel,
          },
        },
      ],
      yAxes: [
        {
          scaleLabel: {
            display: true,
            labelString: yLabel,
          },
          ticks: {
            // 💰 Format Y-axis labels as VND
            callback: function (value) {
              return value.toLocaleString("vi-VN", {
                style: "currency",
                currency: "VND",
                minimumFractionDigits: 0,
              });
            },
          },
        },
      ],
    },
    title: {
      display: true,
      text: title,
    },
  };

  const data = {
    labels: dates,
    datasets: [
      {
        label: "Expenses",
        data: amounts,
        borderColor: "rgb(255,140,0)",
        fill: false,
        tension: 0,
      },
    ],
  };

  return (
    <div className='canvasContainer col-md-12'>
      <Line options={options} data={data} />
    </div>
  );
};

export default LineChart;
