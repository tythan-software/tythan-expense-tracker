function formatNumberToCurrency(amount) {
  if (amount == null || isNaN(amount)) return "₫0";
  return amount.toLocaleString("vi-VN", {
    style: "currency",
    currency: "VND",
    minimumFractionDigits: 0,
  });
}

export const utils = { formatNumberToCurrency };