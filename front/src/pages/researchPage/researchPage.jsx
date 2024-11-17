import React from 'react';
import Header from '../../components/Header'
import InnerUser from './Inner';
import Navbar from '../../components/navbar/Navbar';
import InnerResearch from './researchPage.jsx';

const ResearchPage = ({setPage, page, band, setBand}) => {
    


    return(
        <>
        <Navbar setPage={setPage} page={page}/>
        <div className="body">
            <Header/>
            <div className="outline">
                <InnerResearch band={band} setBand={setBand}/>
            </div>
        </div>
        </>
    )
}


export default ResearchPage;
