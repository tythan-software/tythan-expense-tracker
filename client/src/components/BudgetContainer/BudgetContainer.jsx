import "./styles.css";

import React, { useState, useEffect } from "react";
import { API } from "../../api-service";
import { utils } from "../../utils";

const BudgetContainer = () => {
  const [accessToken] = useState(
    JSON.parse(localStorage.getItem("accessToken"))
  );

  const [budget, setBudget] = useState(0);
  const [statisticsData, setStatisticsData] = useState({});
  const [currentMonthExpenses, setCurrentMonthExpenses] = useState(0);

  useEffect(() => {
    API.fetchBudget(accessToken, setBudget);
    API.fetchStatisticsData(accessToken, setStatisticsData);
  }, []);

  useEffect(() => {
    setCurrentMonthExpenses(statisticsData?.curr_month_expense_sum ?? 0);
  }, [statisticsData]);

  return (
    <>
      {budget.amount > 0 ? (
        <div className='col-md-9 mx-auto'>
          <div
            id='budget-container'
            className='budget-container font-weight-bold'
            data-test='budget-container'
          >
            <div className='progress'>
              <div
                className={`progress-bar ${
                  currentMonthExpenses > budget.amount
                    ? "bg-danger"
                    : "bg-success"
                }`}
                role='progressbar'
                style={{ width: `${(currentMonthExpenses / budget.amount) * 100}%` }}
                aria-valuenow='50'
                aria-valuemin='0'
                aria-valuemax='100'
                data-test='budget-progress-bar'
              ></div>
            </div>
            <div
              style={{ color: "green", float: "left", width: "50%" }}
              data-test='monthly-budget'
            >
              Monthly budget:
              <div>
                <span>{utils.formatNumberToCurrency(budget.amount)}</span>
                <a
                  href={`/update-budget/${budget.id}`}
                  className='font-weight-bold'
                  data-test='update-budget'
                >
                  <span className='badge-pill badge-warning'>✎</span>
                </a>
                <a
                  href={`/delete-budget/${budget.id}`}
                  className='font-weight-bold'
                  data-test='delete-budget'
                >
                  <span className='badge-pill badge-danger'>X</span>
                </a>
              </div>
            </div>

            <div style={{ color: "green" }}>
              Current month expenses:
              <div>
                {utils.formatNumberToCurrency(currentMonthExpenses)}
                {currentMonthExpenses > budget.amount && (
                  <p style={{ color: "red", float: "right" }}>
                    ({utils.formatNumberToCurrency(currentMonthExpenses - budget.amount)} over budget)
                  </p>
                )}
              </div>
            </div>
          </div>
        </div>
      ) : null}
    </>
  );
};

export default BudgetContainer;
