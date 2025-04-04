import React, { useState } from "react";
import "./RestaurantRating.css";

const RestaurantRating = () => {
  const [formData, setFormData] = useState({
    orderOnline: "",
    bookTable: "",
    votes: "",
    location: "",
    cost: "",
    menuItem: "",
    restaurantType: "",
    cuisines: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted", formData);
  };

  return (
    <div className="container">
      <h1>Predict Restaurant Ratings</h1>
      <form className="form-container" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Order Online</label>
          <input type="text" name="orderOnline" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Book Table</label>
          <input type="text" name="bookTable" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Votes</label>
          <input type="text" name="votes" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Location</label>
          <input type="text" name="location" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Cost</label>
          <input type="text" name="cost" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Menu Item</label>
          <input type="text" name="menuItem" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Restaurant Type</label>
          <input type="text" name="restaurantType" onChange={handleChange} />
        </div>
        <div className="form-group">
          <label>Cuisines</label>
          <input type="text" name="cuisines" onChange={handleChange} />
        </div>
        
        <div className="dropdown-button">
          <button type="submit">Predict</button>
        </div>
      </form>
    </div>
  );
};

export default RestaurantRating;
