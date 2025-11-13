import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { API } from "../../api-service";

import CustomForm from "../../components/CustomForm/CustomForm";

const AddBudgetForm = () => {
  const navigate = useNavigate();
  const [accessToken] = useState(
    JSON.parse(localStorage.getItem("accessToken"))
  );
  const [amount, setAmount] = useState(0);
  const handleSubmit = async (e) => {
    e.preventDefault();

    API.createBudget(navigate, accessToken, JSON.stringify({ amount }), setAmount);
  };

  return (
    <>
      <CustomForm
        title='Create Budget:'
        cancelBtn={true}
        onSubmit={handleSubmit}
        dataTestIdForm='create-budget-form'
        dataTestIdSubmitBtn='create-budget-save'
      >
        <p>
          <label>Amount:</label>
          <input
            type='number'
            name='amount'
            className='form-control'
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            data-test='budget-input-amount'
          ></input>
        </p>
      </CustomForm>
    </>
  );
};

export default AddBudgetForm;
