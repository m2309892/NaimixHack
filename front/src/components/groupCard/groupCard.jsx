import React, {useState, useEffect} from 'react';
import './groupCard.css';  

const GroupCard = ({name, special, key, band, setBand}) => {
    const [isChecked, setIsChecked] = useState(false);
    const handleCheckboxChange = () => {
        setIsChecked(!isChecked);
      };

  useEffect(() => {
   if(isChecked) {
    setBand((p) => 
        ({researches: [...p.researches],
        companies: [...p.companies, key] 
        })
    )
   }
    else {
        setBand((p) => 
            ({researches: [...p.researches],
            companies: [...(p.companies.filter(item => item !== key))] 
            }))
    }
  }, [isChecked]);
  

    return (
        <div className="card">
            <div className="field">
            <input 
            className="check"
                type="checkbox" 
                checked={isChecked} 
                onChange={handleCheckboxChange} 
            />
            </div>
            <div>
                <span>{name}</span>
                <span>{special}</span>
            </div>
        </div>
    );
}

export default GroupCard;