import React, { useState, useEffect } from "react";
import MainContainer from "./MainContainer";

const MyComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/data")
      .then((response) => response.json())
      .then((_data) => {
        setData(_data);
        console.log(_data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  // const fetchData = async () => {
  //   try {

  //   } catch (error) {
  //     console.error('Error fetching data:', error);
  //   }
  // };

  return (
    <div>
      {data && <MainContainer videoData={data} />}
      {/* {categories && <MainContainer categories={categories} />
      } */}
    </div>
  );
};
export default MyComponent;
