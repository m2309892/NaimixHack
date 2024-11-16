import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
import UserPage from './pages/userPage/UserPage';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import СompatibilityPage from './pages/сompatibilityPage/СompatibilityPage'
import ResearchPage from './pages/researchPage/researchPage'

function App() {
  const [page, setPage] = useState(0);
  const [band, setBand] = useState([]); //teamId, personId
 
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/userpage/:company_id" element={<UserPage setPage = {setPage} page={page} setBand={setBand} band={band}/>}/>
          {/* <Route path="/ad" element={<AdsPage />}/>
          <Route path="/response" element={<ResponsePage />}/> */}
          <Route path="/compatibility" element={<СompatibilityPage />}/>
          <Route path="/add" element={<ResearchPage  setPage = {setPage} page={page} setBand={setBand} band={band}/>}/>

          </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
