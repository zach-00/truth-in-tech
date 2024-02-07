

function Footer () {
    return (
        <>
        <br></br>
        {/* <!-- Footer --> */}
<footer className="text-center text-lg-start bg-body-tertiary text-muted">
  {/* <!-- Section: Social media --> */}
  <section className="d-flex justify-content-center justify-content-lg-between p-4 border-bottom">
    {/* <!-- Left --> */}
    <div className="me-5 d-none d-lg-block fw-bold">
      <span>Get connected with us on social networks:</span>
    </div>

  </section>
  {/* <!-- Section: Social media --> */}

  {/* <!-- Section: Links  --> */}
  <section className="">
    <div className="container text-center text-md-start mt-5">
      {/* <!-- Grid row --> */}
      <div className="row mt-3">
        {/* <!-- Grid column --> */}
        <div className="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          {/* <!-- Content --> */}
          <h6 className="text-uppercase fw-bold mb-4">
            <i className="fas fa-gem me-3"></i>💎 Truth-In-Tech
          </h6>
          <p>
            Truth-in-Tech is a platform dedicated to providing
             unbiased and informative reviews about technology
              companies.  This helps our users to make informed
               decisions about their career choices and work environments.
                 This website is intended for anyone who is currently in
                  or interested in breaking into the Technology career field.
          </p>
        </div>
        {/* <!-- Grid column --> */}

        {/* <!-- Grid column --> */}
        <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          {/* <!-- Links --> */}
          <h6 className="text-uppercase fw-bold mb-4">
            Tech Stack
          </h6>
            <p className="text-reset">⚡ FastAPI</p>
            <p className="text-reset">⚛️ React-Redux</p>
            <p className="text-reset">🐘 PostgreSQL</p>
            <p className="text-reset"><i className="bi bi-bootstrap-fill"></i> Bootstrap</p>
        </div>
        {/* <!-- Grid column --> */}

        {/* <!-- Grid column --> */}
        <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          {/* <!-- Links --> */}
          <h6 className="text-uppercase fw-bold mb-4">
           👨‍💻 Creators
          </h6>
          <p><i className="fas fa-home"></i>Zach Walkowiak</p>
          <p><i className="fas fa-home"></i>Cory Egan</p>
          <p><i className="fas fa-home"></i>Matt Archbold</p>
          <p><i className="fas fa-home"></i>Adedeji Adetunji</p>
        </div>
        {/* <!-- Grid column --> */}

        {/* <!-- Grid column --> */}
        <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">
          {/* <!-- Links --> */}
          <h6 className="text-uppercase fw-bold mb-4">Contact Us!</h6>
          <p><a href="https://www.linkedin.com/in/zachary-walkowiak-8384a31b5/" className="fas fa-home me-3">Zach's LinkedIn</a> <i className="bi bi-linkedin"></i></p>
          <p><a href="https://www.linkedin.com/in/cory-egan-a980378b/" className="fas fa-home me-3">Cory's LinkedIn</a>  <i className="bi bi-linkedin"></i></p>
          <p><a href="https://www.linkedin.com/in/matt-archbold-690a56278/" className="fas fa-home me-3">Matt's LinkedIn</a> <i className="bi bi-linkedin"></i></p>
          <p><a href="https://www.linkedin.com/in/adedeji-adetunji-900452290/" className="fas fa-home me-3">Adedeji's LinkedIn</a> <i className="bi bi-linkedin"></i></p>
        </div>
        {/* <!-- Grid column --> */}
      </div>
      {/* <!-- Grid row --> */}
    </div>
  </section>
  {/* <!-- Section: Links  --> */}

  {/* <!-- Copyright --> */}

  <div className="text-center p-4">

    <a href="https://gitlab.com/truth-in-tech/truth-in-tech"><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" className="bi bi-gitlab" viewBox="0 0 16 16">
        <path d="m15.734 6.1-.022-.058L13.534.358a.57.57 0 0 0-.563-.356.6.6 0 0 0-.328.122.6.6 0 0 0-.193.294l-1.47 4.499H5.025l-1.47-4.5A.572.572 0 0 0 2.47.358L.289 6.04l-.022.057A4.044 4.044 0 0 0 1.61 10.77l.007.006.02.014 3.318 2.485 1.64 1.242 1 .755a.67.67 0 0 0 .814 0l1-.755 1.64-1.242 3.338-2.5.009-.007a4.05 4.05 0 0 0 1.34-4.668Z"/>
    </svg></a>
    {/* <a className="text-reset fw-bold" href="https://mdbootstrap.com/">MDBootstrap.com</a> */}
  </div>

  {/* <!-- Copyright --> */}
</footer>
{/* <!-- Footer --> */}
</>
    );
}

export default Footer;
