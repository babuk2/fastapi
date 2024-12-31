from fastapi import APIRouter, HTTPException
import router.util as api_pack
import sys

router = APIRouter()

@router.get("/api-data")
async def get_data(api_name: str = "default"):
    try:
        
        api_name_formmat = api_name.replace('-','_').replace('/','')
        # API 호출
        data = api_pack.fetch_data_from_api(api_name_formmat)
        
        GRAPH_YN = {
            'tourist_count'
        }
        
        if api_name_formmat in GRAPH_YN:
            output_type = 'graph'
        else:
            output_type = 'list'
        
        
        return {"api_name": api_name, "output_type": output_type, "data": data}

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
