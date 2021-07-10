import React, { useState } from "react";
import { Link, Redirect } from "react-router-dom";
import { connect } from "react-redux";

import * as TiIcons from "react-icons/ti";
import * as FaIcons from "react-icons/fa";
import UpdateAccount from "./APIServices";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";




function Account({ User, isAuthenticated }) {
  // console.log(User);
  const [formData, setFormData] = useState({
    first_name: User.first_name ? User.first_name : "",
    last_name: User.last_name,
    address: User.address,
    phone: User.phone,
    email: User.email,
  });

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e) => {
    e.preventDefault();
    UpdateAccount.handleUpdate(User.id, formData, setFormData)
    console.log(formData);
  };



  if (!isAuthenticated) return <Redirect to="/login" />;
  return (
    <div className="checkout">
      <div className="breadcrumb-option">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="breadcrumb__links">
                <Link to="/">
                  <TiIcons.TiHome className="homeIcon" /> Home
                </Link>
                <FaIcons.FaAngleRight />
                <span>Profile</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <section className="checkout spad">
        <div className="container">
          <div className="checkout__form">
            <div className="row">
              <div className="col-lg-8">
                <h5>Personal detail</h5>
                <div className="row">
                  <div className="col-lg-6 col-md-6 col-sm-6">
                    <div className="checkout__form__input">
                      <p>
                        First Name <span>*</span>
                      </p>
                      <input
                        type="text"
                        name="first_name"
                        value={formData.first_name}
                        onChange={onChange}
                        required
                      />
                    </div>
                  </div>
                  <div className="col-lg-6 col-md-6 col-sm-6">
                    <div className="checkout__form__input">
                      <p>
                        Last Name <span>*</span>
                      </p>
                      <input
                        type="text"
                        name="last_name"
                        value={formData.last_name}
                        onChange={onChange}
                        required
                      />
                    </div>
                  </div>
                  <div className="col-lg-12">
                    <div className="checkout__form__input">
                      <p>
                        Address <span>*</span>
                      </p>
                      <input
                        type="text"
                        name="address"
                        value={formData.address}
                        onChange={onChange}
                        required
                      />
                    </div>
                    <div className="checkout__form__input">
                      <p>
                        Phone <span>*</span>
                      </p>
                      <input
                        type="text"
                        name="phone"
                        value={formData.phone}
                        onChange={onChange}
                        required
                      />
                    </div>
                    <div className="checkout__form__input">
                      <p>
                        Email <span>*</span>
                      </p>
                      <input
                        type="text"
                        name="email"
                        value={formData.email}
                        onChange={onChange}
                        required
                      />
                    </div>
                  </div>
                  <div className="checkout__form__input padding_left_15">
                    <button
                      type="submit"
                      className="site-btn"
                      onClick={onSubmit}
                    >
                      update
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}


const mapStateToProps = (state) => ({

  User: state.auth.user,
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, {})(Account);
