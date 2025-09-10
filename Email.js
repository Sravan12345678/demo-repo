const nodemailer = require("nodemailer");

let transporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 587,        
  secure: false,    
  auth: {
    user: "pannerusravankumar1234@gmail.com",   
    pass: "kick@001",      
  },
});


let mailOptions = {
  from: "pannerusravankumar1234@gmail.com",
  to: "v.nagabharathgmail.com",
  subject: "Hello from Nodemailer",
  text: "This is a test email sent using Nodemailer!",
};


transporter.sendMail(mailOptions, (error, info) => {
  if (error) {
    return console.log("Error:", error);
  }
  console.log("Email sent:", info.response);
});
